import pandas as pd
import numpy as np

def load_data(path):
    df = pd.read_csv(path)
    return df

#frequency of the unique values in each column
def clean_data(df, num_col, cat_col):
    df = df.drop_duplicates()
    for col in num_col:
        mean_value = df[col].mean()
        df[col] = df[col].apply(lambda x: mean_value if x < 0 else x)
        df[col].fillna(df[col].mean(), inplace=True)
        Q1 = df[num_col].quantile(0.25)
        Q3 = df[num_col].quantile(0.75)
        IQR = Q3 - Q1
        outlier = ~((df[num_col] < (Q1 - 1.5 * IQR)) | (df[num_col] > (Q3 + 1.5 * IQR))).all(axis=1)
        df = df[outlier]
    
    for col in cat_col:
        df[col].replace({'Any': df[col].mode()[0], 'NONE': df[col].mode()[0]}, inplace=True)
        df[col].fillna(df[col].mode()[0], inplace=True)
    
    return df


housing_path = 'd:/Maria_iti/day 10/housingNoisy.csv'
salary_path = 'd:/Maria_iti/day 10/salariesNoisy.csv'

housing_df = load_data(housing_path)
num_house_col = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
cat_house_col = ['ocean_proximity']
housing_cleaned = clean_data(housing_df, num_house_col, cat_house_col)
housing_cleaned.to_csv('cleaned_housing.csv', index=False)

salary_df = load_data(salary_path)
salary_df.columns = ['index', 'gender', 'employment_status', 'age', 'education', 'experience', 'salary']
cat_salary_col = ['gender', 'employment_status', 'education']
num_salary_col = ['age', 'experience', 'salary']
salary_cleaned = clean_data(salary_df, num_salary_col, cat_salary_col)
salary_cleaned.to_csv('cleaned_salary.csv', index=False)

print('Cleaned Housing Data:')
print(housing_cleaned.head())
print('\nCleaned Salary Data:')
print(salary_cleaned.head())
