import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

np.random.seed(0)
X = np.random.rand(100, 1) * 10 
y = 2 * X + 1 + np.random.randn(100, 1) * 2 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Mean Squared Error:", mse)

plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
# plt.show()
# -------------------------------------------------------------------------------------------------

# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# import matplotlib.pylab as plt
# from sklearn.model_selection import train_test_split
# dataset=pd.read_csv('Techniques of ML/HousingFloat.csv')
# x = dataset[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms','Avg. Area Number of Bedrooms', 'Area Population']]
# y=dataset['Price']
# x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=1)
# lRModel=LinearRegression()
# lRModel.fit(x_train, y_train)
# print('coefficient of determination:', lRModel.coef_)
# print(pd.DataFrame(lRModel.coef_, x_train.columns, columns = ['Coeff']))
# predictions = lRModel.predict(x_test)

# from sklearn import metrics
# print("mean_absolute_error is "+ str(metrics.mean_absolute_error(y_test, predictions)))
# print("mean_squared_error is "+ str (metrics.mean_squared_error(y_test, predictions)))
# print("mean_squared_root is "+ str(np.sqrt(metrics.mean_squared_error(y_test, predictions))))

# # -----------------with String---------
import pandas as pd
# It must convert to One-Hot encoding for categorical data
# Example
# idx color
# 0   blue
# 1   green
# 2   green
# 3   red
# TO
# idx blue green red
# 0   1    0     0
# 1   0    1     0
# 2   0    1     0
# 3   0    0     1

# data = pd.DataFrame({
#     'Color': ['Red', 'Blue', 'Green', 'Red', 'Green'],
#     'Size': ['Small', 'Medium', 'Large', 'Medium', 'Small'],
#     'Price': [10, 20, 15, 25, 12],
#     'Quantity': [100, 50, 75, 60, 90]
# })

# data_encoded = pd.get_dummies(data, columns=['Color', 'Size'])
# print(data_encoded)

# -----

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pylab as plt
dataset=pd.read_csv('Techniques of ML/salaries.csv')
x = dataset[['id','sex','rk','years','dg','yd']]
y= dataset['salary']
# Convert categorical variable into dummy/indicator variables and drop one in each category Like "ENCODING ": 
x = pd.get_dummies(data=x, drop_first=True)
# print(x.head(5))
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=1)
lRModel=LinearRegression()
lRModel.fit(x_train, y_train)
print(pd.DataFrame(lRModel.coef_, x_train.columns, columns = ['Coeff']))
predictions = lRModel.predict(x_test)
plt.scatter(y_test, predictions)
plt.show()
from sklearn import metrics
print("mean_absolute_error is "+ str(metrics.mean_absolute_error(y_test, predictions)))
print("mean_squared_error is "+ str (metrics.mean_squared_error(y_test, predictions)))
print("mean_squared_root is "+ str(np.sqrt(metrics.mean_squared_error(y_test, predictions))))