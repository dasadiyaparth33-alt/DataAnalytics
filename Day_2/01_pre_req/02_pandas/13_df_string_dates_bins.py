import pandas as pd
import numpy as np

df_raw = pd.DataFrame({
    'raw_title' : [' PROD_101_Laptop_v2 ', 'prod_102_Mobile_v1', ' PROD_103_Tablet_v3 ','prod_104_Monitor_v2']
})

# cleaning whitespace and standardize casing

df_raw['clean_title'] = df_raw['raw_title'].str.strip().str.upper()
print(df_raw)

print("="*50)
# Extract structured components using regular expression
regex_pattern = r"PROD_(?P<ID>\d+)_(?P<Category>\w+)_(?P<Version>V\d+)"
df_extrected = df_raw['clean_title'].str.extract(regex_pattern)
print(df_extrected)

print("="*50)
df_strings = pd.concat([df_raw['clean_title']], df_extrected, axis=1)
print(df_strings)

print("="*50)
df_events = pd.DataFrame({
    'timestamp_str': []
})
