import pandas as pd
import numpy as np

df_wide = pd.DataFrame({
    'player': ['Kohli','Rohit','Gill'],
    'fifties' : [220,180,45],
    'hundreds' : [80,31,8]
})
print(df_wide)
print("="*50)
df_melted = df_wide.melt(id_vars='player', var_name='score_type',value_name='count')
print("====Melted Formate====")
print(df_melted)
print("="*50)
df_pivoted = df_melted.pivot(index='player',columns = 'score_type',values='count')
print(df_pivoted)
print("="*50)

df_multi =pd.DataFrame({
    'Q1':[10,20],
    'Q2' : [15,25]
}, index = ['Company_A','Company_B'])
print(df_multi)
print("="*50)

stacked = df_multi.stack()
print("===Stacked Series===")
print(stacked)
print("="*50)

unstacked = stacked.unstack()
print("===Unstacked Data Frame===")
print(unstacked)