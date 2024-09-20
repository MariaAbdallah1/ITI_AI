import pandas as pd
from sklearn.datasets import load_breast_cancer
data = load_breast_cancer()
X = data.data
y = data.target
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)
from sklearn.naive_bayes import GaussianNB
nBmodel = GaussianNB()
nBmodel.fit(X_train , y_train)
y_predicted = nBmodel.predict(X_test)
from sklearn import metrics 
print(metrics.accuracy_score(y_predicted , y_test))

from sklearn.metrics import confusion_matrix
print(pd.DataFrame(
    confusion_matrix(y_test, y_predicted),
    columns=['Predicted Not cancer', 'Predicted cancer'],
    index=['Actual Not cancer', 'Actual cancer']
))