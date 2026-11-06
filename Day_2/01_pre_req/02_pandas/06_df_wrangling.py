'''
what is data wrangling?
Discovering
structuring
cleaning
enriching
validating
publishing

'''
import pandas as pd
import numpy as np

#load beverages dataset
df_drinks = pd.read_csv("supportFiles/drinks.csv")
print(df_drinks.head(5))

print("="*50)
print(df_drinks.sort_values(by="spirit_servings",ascending=False).head()[["country","spirit_servings","continent"]])
print(df_drinks.head(5))
    
print("="*50)
print(df_drinks["continent"].value_counts)

print("="*50)

print("--High spirit Consumption(>200)(European Countries)--")
mask_europe = (df_drinks["continent"] == "Europe") & (df_drinks["spirit_servings"] > 200)
df_high_spirit_europe = df_drinks[mask_europe]
print(df_high_spirit_europe[["country","spirit_servings","continent","total_litres_of_pure_alcohol"]])

print("="*50)
mask_asian_african = (df_drinks["continent"] == "Asia")| (df_drinks["continent"]=="Africa")
df_asian_african = df_drinks[mask_asian_african]
print(df_asian_african[["country","spirit_servings","continent","total_litres_of_pure_alcohol"]])

print("="*50)
#Second Method
mask_asian_african = (df_drinks["continent"]).isin(["Asia","Africa"])
df_asian_african = df_drinks[mask_asian_african]
print(df_asian_african[["country","spirit_servings","continent","total_litres_of_pure_alcohol"]])

print("="*50)
print("shape: ",df_asian_african.shape)
print("="*50)
print("Value Counts: ",df_asian_african["continent"].value_counts())
print("="*50)

