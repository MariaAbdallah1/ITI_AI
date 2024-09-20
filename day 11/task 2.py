import os
import numpy as np
from skimage.feature import hog
from skimage import color, io
from skimage.transform import resize

data_path = 'd:/Maria_iti/day 11/brain_tumor_dataset'

def extract_features_from_folder(folder):
    images = []
    labels = []
    for label in os.listdir(folder):
        label_folder = os.path.join(folder, label)
        if not os.path.isdir(label_folder):
            continue
        for filename in os.listdir(label_folder):
            file_path = os.path.join(label_folder, filename)
            try:
                img = io.imread(file_path)
                if len(img.shape) == 3 and img.shape[2] == 3:
                    img_gray = color.rgb2gray(img)
                elif len(img.shape) == 2:
                    img_gray = img
                else:
                    print(f"Unsupported image format in file: {file_path}")
                    continue

                img_resized = resize(img_gray, (128, 128), anti_aliasing=True)
                
                features = hog(img_resized, visualize=False, feature_vector=True)
                images.append(features)
                labels.append(label)
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")
                continue
    
    return np.array(images), np.array(labels)

features, labels = extract_features_from_folder(data_path)

labels = np.where(labels == 'yes', 1, 0)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

models = {
    "KNN": KNeighborsClassifier(),
    "Decision Tree": DecisionTreeClassifier(),
    "Naïve Bayes": GaussianNB()
}

from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import cross_val_score, KFold

results = {}
for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    results[model_name] = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "Confusion Matrix": confusion_matrix(y_test, y_pred),
        "F1 Score": f1_score(y_test, y_pred),
        "Precision": precision_score(y_test, y_pred),
        "Recall": recall_score(y_test, y_pred)
    }

kf = KFold(n_splits=10, shuffle=True, random_state=42)

def cross_validate_model(model):
    scores = cross_val_score(model, features, labels, cv=kf, scoring='accuracy')
    return scores.mean()

cv_scores = {model_name: cross_validate_model(model) for model_name, model in models.items()}

for model_name in models.keys():
    print(f"\n{model_name}:")
    print(f"Accuracy: {results[model_name]['Accuracy']}")
    print(f"Confusion Matrix:\n{results[model_name]['Confusion Matrix']}")
    print(f"F1 Score: {results[model_name]['F1 Score']}")
    print(f"Precision: {results[model_name]['Precision']}")
    print(f"Recall: {results[model_name]['Recall']}")
    print(f"K-Fold Cross-Validation Score: {cv_scores[model_name]}")
