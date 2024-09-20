# import pandas as pd
# from mlxtend.frequent_patterns import apriori, association_rules

# data = {'milk': [1, 1, 0, 1, 0], #sample1
#         'bread': [1, 0, 1, 1, 1],
#         'butter': [0, 1, 1, 0, 0],
#         'cheese': [0, 1, 0, 1, 0],
#         'eggs': [1, 0, 1, 1, 1]}

# df = pd.DataFrame(data)

# frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)
# print("Frequent Itemsets:\n", frequent_itemsets)
# rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)
# print("\nAssociation Rules:\n", rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
# ---------------------------------------------------
# import pandas as pd
# from mlxtend.frequent_patterns import apriori, association_rules

# df = pd.read_csv('Techniques of ML/store_data.csv',header=None)

# from mlxtend.preprocessing import TransactionEncoder

# transactions = df.stack().groupby(level=0).apply(list).tolist()# Convert the DataFrame rows to a list of lists (transactions)
# # # Use TransactionEncoder to encode the data into a binary matrix
# te = TransactionEncoder()
# te_ary = te.fit(transactions).transform(transactions)
# # print(te_ary)
# # # # Convert the array back into a DataFrame
# transaction_df = pd.DataFrame(te_ary, columns=te.columns_)
# # print(transaction_df.head())
# frequent_itemsets = apriori(transaction_df, min_support=0.2, use_colnames=True)
# print(frequent_itemsets)
# rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.7)

# print(rules)

# -----------------------------------------
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import re
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from mlxtend.preprocessing import TransactionEncoder
from mpl_toolkits.mplot3d import Axes3D
import networkx as nx

basket = pd.read_csv("Techniques of ML/Groceries_dataset.csv")

basket.itemDescription = basket.itemDescription.transform(lambda x: [x])
basket = basket.groupby(['Member_number','Date']).sum()['itemDescription'].reset_index(drop=True)
# print(basket)
encoder = TransactionEncoder()
transactions = pd.DataFrame(encoder.fit(basket).transform(basket), columns=encoder.columns_)


frequent_itemsets = apriori(transactions, min_support= 6/len(basket), use_colnames=True, max_len = 2)
rules = association_rules(frequent_itemsets, metric="lift",  min_threshold = 1.5)
print(rules.head())
print("Rules identified: ", len(rules))