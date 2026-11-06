import pandas as pd
import numpy as np

df_drinks = pd.read_csv("supportFiles/drinks.csv")
print(df_drinks.head())
print("="*50)


print("="*50)

# split-apply-combined workflow

continent_stats = df_drinks.groupby('continent').agg(
    avg_beer = ("beer_servings","mean"),
    max_wine = ("wine_servings","max"),
    total_pure_alcohol = ("total_litres_of_pure_alcohol","sum"),
    country_count = ("country","count")
)

print("---Continental Drink Aggergation---")
print(continent_stats)

print("---Continental Drink Aggergation 2---")
continent_stats_2 = df_drinks.groupby('continent').agg({
    "beer_servings" : ['mean','max','std'],
    "wine_servings" : ['sum'],
    "country" : ['count']
})
print(continent_stats_2)
