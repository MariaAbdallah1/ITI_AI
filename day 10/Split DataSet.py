import pandas as pd
from sklearn.model_selection import train_test_split
housing = pd.read_csv("CommonStepsML/housing.csv")
# print(housing.head())
 
#output
y= housing.median_income
 
#input
x=housing.drop('median_income',axis=1)
 
#splitting
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2) #50,60,70
#ds_train(80%),ds_test(20%), ds_train_label(80%), ds_test_label(20%)
 
#printing shapes of testing and training sets :
print("shape of original dataset :", housing.shape)
print("shape of input - training set", x_train.shape) 
print("shape of output - training set", y_train.shape)
print("shape of input - testing set", x_test.shape)
print("shape of output - testing set", y_test.shape)