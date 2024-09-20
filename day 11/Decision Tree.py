# errorin write_png() install this package from source  https://graphviz.gitlab.io/download/
# Add path to environment  
from sklearn import tree 
import pandas as pd 
import pydotplus # Decision Tree Graph
import matplotlib.image as pltimg
import matplotlib.pyplot as plt

golf_df = pd.DataFrame()
golf_df['Outlook'] = ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy', 
                     'overcast', 'sunny', 'sunny', 'rainy', 'sunny', 'overcast',
                     'overcast', 'rainy']

golf_df['Temperature'] = ['hot', 'hot', 'hot', 'mild', 'cool', 'cool', 'cool',
                         'mild', 'cool', 'mild', 'mild', 'mild', 'hot', 'mild']

golf_df['Humidity'] = ['high', 'high', 'high', 'high', 'normal', 'normal', 'normal',
                      'high', 'normal', 'normal', 'normal', 'high', 'normal', 'high']

golf_df['Windy'] = ['false', 'true', 'false', 'false', 'false', 'true', 'true',
                   'false', 'false', 'false', 'true', 'true', 'false', 'true']

golf_df['Play'] = ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 
                  'yes', 'yes', 'no']

one_hot_data = pd.get_dummies(golf_df[ ['Outlook', 'Temperature', 'Humidity', 'Windy'] ])#print the new dummy data
# print(one_hot_data.Outlook_overcast,golf_df.Play)

dtree = tree.DecisionTreeClassifier()
dtree = dtree.fit(one_hot_data, golf_df['Play'])
data = tree.export_graphviz(dtree, out_file=None, feature_names=list(one_hot_data.columns.values))
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')

img=pltimg.imread('mydecisiontree.png')
imgplot = plt.imshow(img)
plt.show()