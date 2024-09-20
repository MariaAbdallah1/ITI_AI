import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler, LabelEncoder
from sklearn.impute import SimpleImputer

data = {
    "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10],
    "numeric_column": [10, 15, 20, 25, 30, 35, 40, 45, 50, 30, 30],
    "column_with_missing_values": [15, 25, None, 35, 45, 55, None, 65, 75, 85, 85],
    "categorical_column": ["Category A", "Category B", "Category A", "Category C", "Category B", "Category A", "Category C", "Category B", "Category A", "Category C", "Category C"],
    "HighNumericalValues":[500, 6000, 800, 100, 102, 140, 106, 180, 200, 202,202],
    'age': [0, 15, 20, -25, 30, 35, 40, 45, 5000, 300,300],
}
data = pd.DataFrame(data)
#Handling Missing Values
def MissingValues():
    global data
    imputer = SimpleImputer(strategy="mean")
    data["column_with_missing_values"] = imputer.fit_transform(data[["column_with_missing_values"]])
    print(data)
# MissingValues()
#Outlier Detection and Treatment
# Detect outliers using IQR 
def IQRSample(data):

    # data = [-75000,40000, 50000,99999, 10000000, 20] # [-40000 20 75 50000 99999 10000000]
    q1 = np.percentile(data, 25)
    q3 = np.percentile(data, 75)
    q2 = np.percentile(data, 50)
    iqr = q3 - q1
    print(q1, q3)
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = [x for x in data if x <= lower_bound or x >= upper_bound]
    print("Dataset:", data)
    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)
    print("Outliers:", outliers)
    return outliers
# IQRSample()
# Detect outliers using Z-score a
def CalcZscore():
    exam_scores = [85, 88, 92, 78, 95, 100, 600, 82, 79, 105, 88, 86, 90, 92, 500, 87, 84, 81, 98, 110, 300]
    mean_score = np.mean(exam_scores)
    std_dev = np.std(exam_scores)
    z_scores = [(x - mean_score) / std_dev for x in exam_scores]
    threshold = 2
    # outliers = [x for x, z in zip(exam_scores, z_scores) if abs(z) > threshold]
    outliers=IQRSample(exam_scores)
    print("Z-Scores:", z_scores)
    print("Outliers:", outliers)
    plt.scatter(np.linspace(min(exam_scores),max(exam_scores),len(exam_scores)), exam_scores)
    plt.show()
#using zscore lib for update in dataframe
def CalcZcoreByLib():
    # data = [85, 88, 92, 78, 95, 100, 600, 82, 79, 105, 88, 86, 90, 92, 500, 87, 84, 81, 98, 110, 300]
    global data
    z_scores = np.abs(stats.zscore(data["numeric_column"]))
    print(z_scores)
    data_outliers = data[z_scores > 2]
    c=input(f'The outlier is {data_outliers}, Do you want to remove it press (r)?')
    if c=='r':
        data=data.drop(data_outliers.index)
        print(data.head(10))

def standardScaler():
    # data = [85, 88, 92, 78, 95, 100, 600, 82, 79, 105, 88, 86, 90, 92, 500, 87, 84, 81, 98, 110, 300]
    global data
    scaler = StandardScaler()
    data["standardized_column"] = scaler.fit_transform(data[["numeric_column"]])
    data['standardized_column2']=scaler.fit_transform(data[['HighNumericalValues']])
    print(data[['numeric_column','standardized_column','HighNumericalValues','standardized_column2']])
    
# Data Scaling and Normalization
# 
# Use MinMaxScaler to normalize data
def MinMaxNormSample():
    data = pd.DataFrame({'feature': [10, 20, 30, 40, 50]})
    min_value = data['feature'].min() #10
    max_value = data['feature'].max() #50
    data['scaled'] = (data['feature']- min_value) / (max_value - min_value) 
    print(data)

#use MinMax to specific Min and Max Values
def MinMaxNormToCustomRange(newmin = -1, newmax = 1):
    data = pd.DataFrame({'feature': [10, 20, 30, 40, 50]})
    data['scaled'] = newmin + (data['feature'] - data['feature'].min()) * (newmax - newmin) / (data['feature'].max() - data['feature'].min())
    print(data) 
def MinMaxNormLib():
    global data
    minmax_scaler = MinMaxScaler()
    data["MinMaxnormalized_column"] = minmax_scaler.fit_transform(data[["numeric_column"]])
    data["MinMaxnormalized_column2"] = minmax_scaler.fit_transform(data[["HighNumericalValues"]])
    print(data[['numeric_column','MinMaxnormalized_column','HighNumericalValues','MinMaxnormalized_column2']])

def DescimalScaling():
    data1= pd.DataFrame({'feature': [15, 200, 3000, 40, 50000] })
    data = pd.DataFrame({'feature': [10, 20, 30, 40, 50]})
    max_value = data['feature'].abs().max()
    j = len(str(int(max_value)))  
    scaling_factor = 10 ** j
    data['scaled'] = data['feature'] / scaling_factor
    print(data)