import numpy as np
import pandas as pd

list = [2,3,-1,4]
total = np.cumsum(list) #[2 5 4 8]
print(total)

print("="*50)
np.random.seed(42)
dates = pd.date_range(start="2026-01-01",periods=100,freq="D")
prices = 150 + np.random.randn(100).cumsum()

df_stocks = pd.DataFrame({"Date":dates,"Price":prices}).set_index("Date") 
print(df_stocks)
print("="*50)

# Rolling Window
df_stocks["7D_MA"] = df_stocks["Price"].rolling(window=7).mean()
df_stocks["7D_STD"] = df_stocks["Price"].rolling(window=7).std()

print(df_stocks.head(10))
print("="*50)
