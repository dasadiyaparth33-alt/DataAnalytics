# it all use for feature engineering stage in data preprocessing
import pandas as pd
df_drinks = pd.read_csv("supportFiles/drinks.csv")

print("="*50)
print("--- Dataset Preview (Head)---")
print(df_drinks.head())

#to see index
print("="*50)
print("Index Objects:\n",df_drinks.index)
print("="*50)

#column names
print("Column Names:\n" ,df_drinks.columns)

#datatypes
print("Data types: \n", df_drinks.dtypes)

print("="*50)
print("Axes: \n",df_drinks.axes)  #axes gives index information and column information
print("="*50)

print(df_drinks.describe())
print("="*50)

print("---Transfos---")
print(df_drinks.describe().T)

print("="*50)
print(df_drinks.describe().T[["mean","std","min","max"]])
print("="*50)

df_subset = df_drinks[["country","continent","total_litres_of_pure_alcohol"]].copy()
print(df_subset.head(3))
print("="*50)

df_subset["status"] = "Evaluated"
print(df_subset.head(5))
print("="*50)

df_subset.insert(1,"region_category",value="Standard Market")
print(df_subset.head(5))
print("="*50)

df_subset["boosted_liters"] = df_subset["total_litres_of_pure_alcohol"].add(2.5)
print("="*50)
print(df_subset.head(5))
