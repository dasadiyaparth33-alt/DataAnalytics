import numpy as np
import pandas as pd

print("="*50)
# Ordern Quantities Matrix (Rows: Orders, Columns: Items) 
df_orderd = pd.DataFrame({
    'item_A': [2,1,4],
    'item_B': [0,3,1],
    'item_C': [5,2,0]
}, index=['Order_1','Order_2','Order_3'])
print(df_orderd)
print("="*50)
print(df_orderd.T)
# Unit price series
s_price = pd.Series([10.0,25.0,5.0], index=['item_A','item_B','item_C'])
print(s_price)
print("="*50)

# Matrix- Vector dot product
df_total = df_orderd.dot(s_price)
print(df_total)
print("="*50)

df_metrics = pd.DataFrame({
    'A' : np.random.randint(1,100,5),
    'B' : np.random.randint(1,100,5),
    
})
print("="*50)


np.random.seed(42)
df_time_series = pd.DataFrame({
    'daily_sales':[100,120,115,130,140,125,150,160,155,170]
})

df_time_series['3D_moving_avg'] = df_time_series['daily_sales'].rolling(window=3).mean()
df_time_series['Running_Total'] = df_time_series['daily_sales'].expanding(min_periods=1).sum()

print("---Rolling & Expanding Window Output---")
print(df_time_series)
print("="*50)