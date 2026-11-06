import pandas as pd
import numpy as np

'''
What is a DataFrame?
A DataFrame is a two-dimensional, size-mutable, and heterogeneous tabular data structure with labeled axes (rows and columns). 
'''

df_cricket = pd.DataFrame({
    "name": ["Shubhamn Gill","Deepti Sharma","Mohammed Siraj","Rohit Sharma"],
    "age": [23,27,22,40],
    "gender": ["Male","Female","Male","Male"]
})

print("--In Memory DataFrame--")
print(df_cricket)
print("="*50)

print("Extract the age column as a series")
age_series = df_cricket["age"]
print(age_series)
print(type(age_series))
print("="*50)

print("Descibe the age column:")
print(df_cricket["age"].describe())
print("="*50)

print("Inforamtion about Data Frame: ")
print(df_cricket.info())
print("="*50)

print("Shape of Data Frame: ",df_cricket.shape)
print("Data type of name column: ",df_cricket["name"].dtype)