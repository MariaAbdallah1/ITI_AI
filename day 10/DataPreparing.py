import pandas as pd
s = pd.Series(['cat', 'cow', 'dog'])
# print("Series:\n", s)
# print("Mapping: ")
# print(s.map({'cat': 'kitten', 'cow': 'calf'}))
# -----------

s = pd.Series(['lily', 'rose','lotus'])
# print(s.map('This is a {}'.format))
# --------------------

df = pd.DataFrame(
	[('carrot', 'red', 1), 
	('papaya', 'yellow', 0),
	('mango', 'yellow', 0), 
	('apple', 'red', 0)
	], 
	columns=['species', 'color', 'type']
)
# print("Dataframe before Mapping: ")
# print(df)

mappings = {
	'carrot': 'veg',
	'papaya': 'fruit'
}

df['type_name'] = df['species'].map(mappings)
# print("Dataframe after Mapping: ")
# print(df)

# Encoding Categorical Data (Label Encoding) 
def LabelEncodingSimple():
    data = {"Color": ["Red", "Green", "Blue", "Green", "Red"]}
    df = pd.DataFrame(data)
    color_mapping = {"Red": 0, "Green": 1, "Blue": 2}
    df["Color_Encoded"] = df["Color"].map(color_mapping)
    # print("Original Data:")
    # print(df["Color"])
    # print("Encoded Data:")
    # print(df["Color_Encoded"])
    print(df.head())
# KNN feature [color=]  Testing point color =0    point color=1    point color=2
# --------------------------------
def HotEncoding():
    data = pd.DataFrame({'Color': ['Red', 'Green', 'Blue', 'Green', 'Red']})
    encoded_data = pd.get_dummies(data, columns=['Color'])
    print(data)
    print(encoded_data)
# -----------------------
ecommerce_df = pd.DataFrame({
    'customer_id': [101, 102, 103],
    'full_name': ['Alice Johnson', 'Bob Smith', 'Charlie Brown'],
    'email_address': ['alice@example.com', 'bob@example.com', 'charlie@example.com'],
    'purchase_amount': [250, 400, 150]
})

crm_df = pd.DataFrame({
    'id': [102, 104, 105],
    'name': ['Bob Smith', 'Diana Prince', 'Evan Wright'],
    'email': ['bob@example.com', 'diana@example.com', 'evan@example.com'],
    'last_contact_date': ['2024-03-15', '2024-01-22', '2024-02-14']
})

# Mapping columns to match CRM dataset
mapped_ecommerce_df = ecommerce_df.rename(columns={
    'customer_id': 'id',
    'full_name': 'name',
    'email_address': 'email'
})

# print("Mapped E-Commerce Dataset:")
# print(mapped_ecommerce_df)

# Merging the datasets on 'id', 'name', and 'email'
merged_df = pd.merge(mapped_ecommerce_df, crm_df, how='inner')
print("\nMerged Dataset:")
print(merged_df)