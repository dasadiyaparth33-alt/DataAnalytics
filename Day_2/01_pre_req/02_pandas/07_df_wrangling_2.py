'''
Missing values
1. Identifiy
2. Drop
3. Impute
'''
import pandas as pd
import numpy as np

df_titanic = pd.read_csv("supportFiles/titanic.csv")
print(df_titanic.head())
print("="*50)
print("--Missing Values Count Per Column--")
print(df_titanic.isnull().sum())
print("="*50)
median_age = df_titanic["Age"].median() #it is not sensitive to outliers that's why we use median 
df_titanic["Age_Imputed"] = df_titanic["Age"].fillna(median_age) 
df_titanic["Cabin_Filled"] = df_titanic["Cabin"].fillna("Unknown") 
print("After Imputation Age: ",df_titanic["Age_Imputed"].isna().sum())
print("After Imputation Cabin: ",df_titanic["Cabin_Filled"].isna().sum())
print("="*50)

print(df_titanic.head()[["Age","Age_Imputed","Cabin","Cabin_Filled"]])
df_titanic_cleaned = df_titanic.copy()
# 1
df_titanic_cleaned["Age"] = df_titanic_cleaned["Age_Imputed"]
df_titanic_cleaned["Cabin"] = df_titanic_cleaned["Cabin_Filled"]
# 2
df_titanic_cleaned[["Age","Cabin"]] = df_titanic_cleaned[["Age_Imputed","Cabin_Filled"]]
# 3
df_titanic_cleaned = df_titanic_cleaned.assign(Age = df_titanic_cleaned["Age_Imputed"],
                                               Cabin = df_titanic_cleaned["Cabin_Filled"])
print(df_titanic_cleaned.isna().sum())
print("="*50)
df_titanic_cleaned = df_titanic_cleaned.drop(columns=["Age_Imputed","Cabin_Filled"])
print("="*50)
print(df_titanic_cleaned.isna().sum())

print("="*50)
print(df_titanic_cleaned["Embarked"].value_counts())
print("="*50)

most_used = df_titanic_cleaned["Embarked"].mode()
print(most_used)
print(most_used[0])

"""
Embarked
S    644 : Southampton (England)
C    168 : Cherbourg (France) - The First stopover
Q     77 : Queenstown (Ireland)
"""
print("="*50)
df_titanic_cleaned["Embarked"] = df_titanic_cleaned["Embarked"].fillna(df_titanic_cleaned["Embarked"].mode()[0])
print(df_titanic_cleaned.isna().sum())
