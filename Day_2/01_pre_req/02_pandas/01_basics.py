'''
when you work with one dimenssional array then Series
when you work with Two dimensional arry then use data frame
'''
# pip install pandas
# 

import pandas as pd
import numpy as np

#Instantiating empty series
empty_s = pd.Series(dtype = np.float64)
print("Empty Series: ", empty_s)

#String payload(Objects)
players = ['Sachin','Saurav','Rahul','Sewag']
players_s = pd.Series(players, name="Players")
print("\n---String Series---")
print(players_s)

#integer payload
scores = [100,200,678,598]
scores_a = pd.Series(scores, name="Scores")
print("\n--- Integer Series---")
print(scores_a)

#Vectorization and reduction

costs = pd.Series([3.43,56.7,23.4,34.3,22.4], name='Costs')
print("Original Costs:\n",costs)
print("Sum of all Costs:\n",costs.sum())
print("Product of all Costs:\n",costs.product())
print("Min value of Costs:\n",costs.min())
print("Max value of  Costs:\n",costs.max())



