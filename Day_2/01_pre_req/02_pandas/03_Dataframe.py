import pandas as pd
import numpy as np

df_titanic = pd.read_csv("supportFiles/titanic.csv")
print("Loaded Titanic CSV Shape: ",df_titanic.shape)
print(df_titanic.head(3))

#Export Dataframe to Excel spredSheet
df_titanic.to_excel("supportFiles/titanic.xlsx", sheet_name="passengers", index=False)

# Reload Dataframe from excel  spredsheet
df_from_excel = pd.read_excel("supportFiles/titanic.xlsx", sheet_name="passengers")
print("\nReloaded Excel Passengers shape: ",df_from_excel.shape)