import pandas as pd
import numpy as np

#setting explicit indexcolumn on load
df_index = pd.read_csv("supportFiles/drinks.csv", index_col="country")
print(" Custom Country Index Preview:\n", df_index.head(5))
print("="*50)

#look at ram footprint
mem_original_surface = df_index.memory_usage().sum()
print("Original memory used: ",mem_original_surface)
print("="*50)

mem_original_element_level = df_index.memory_usage(deep=True)
print("Original memory used at element level: ",mem_original_element_level.head())

print("="*50)
print(df_index.info())
print("="*50)

print("{0:35}{1:15}{2:15}{3:<15}{4:<15}".format("Column Name", "Min", "Max", "type","Can Hold"))
#for col in df_index.select_dtypes(include=[np.number]).columns:
for col in df_index.select_dtypes(include=['int64','float64']).columns:
    dt = df_index[col].dtype
    max_can_hold = np.iinfo(dt).max if np.issubdtype(dt, np.integer) else np.finfo(dt).max
    print("{0:<35}{1:<15}{2:<15}{3:<15}{4:<15}".format(col.capitalize(),df_index[col].min(), df_index[col].max(),dt.__str__(), max_can_hold))
print("="*50)

#Down casting
print("Down Casting:")
df_optimized = df_index.copy()
for col in df_optimized.select_dtypes(include=[np.number]).columns:
    dt = df_optimized[col].dtype
    cast_to_str = "integer" if np.issubdtype(dt,np.integer) else "float"
    df_optimized[col] = pd.to_numeric(df_optimized[col],downcast=cast_to_str)
print("="*50)

print(df_optimized.info())
print("="*50)

mem_optimized_surface = df_optimized.memory_usage().sum()
print("Optimized memory used: ",mem_optimized_surface)
print("="*50)

mem_optimized_element_level = df_optimized.memory_usage(deep=True)
print("Optimized memory used at element level: ",mem_optimized_element_level.head())