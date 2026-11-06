'''
numpy slicing is a powerful feature that allows you to extract specific portions of an array.
Advantage of numpy slicing include:
1. zero-copy views: sharing underlying buffer memory with the original array,
   which saves memory and improves performance.
2. flexible Indexing: Teturns a view of the original array
3. Boolean Indexing: Allows you to select elements based on conditions,making it easy to filter data.

'''

import numpy as np

sensor_reading = np.arange(9)
print("Original Array: ", sensor_reading)

sensor_reading[3] = 888
print("Original Array: ", sensor_reading)

sensor_reading[3] = 3
print("Sliced Array: ", sensor_reading[2:5])

#tensor change
sensor_reading[2:5] = 3
print("Modified Array: ", sensor_reading)

print("-"*50)

values = np.arange(10,101,10)
print("Original Array: ", values)
print("Values[2]: ", values[2])# accessing single element
print("Values[2:]: ", values[2:]) # slicing from index 2 to end
print("Values[2:5]: ", values[2:5]) # Slicing
print("Values[:5]: ", values[:5]) # Slicing from the start to index 4
print("Values[1:8:2]: ", values[1:8:2]) # slicing with a step 2
print("Values[::3]: ", values[::3]) # Slicing with setp 3
print("Values[-1]: ", values[-1])# accessing last elements
print("Values[-3:]: ", values[-3:]) # Slicing the last three elements
print("Values[:-3]: ", values[:-3]) # Slicing all but last three except
print("Values[-5:-2]: ", values[-5:-2])
print("Values[-2:-5]: ", values[-2:-5])
print("Values[-2:-5:-1]: ", values[-2:-5:-1]) # Slicing in the reverse order from second last to the third last
print("Values[-5:-2:-1]: ", values[-5:-2:-1]) # it's give empty array
print("Values[-2::-1]: ", values[-2::-1]) # Slicing in the reverse order from the second last to first
print("Values[::-1]: ", values[::-1]) # Slicing in riverse order
print("-"*50)

feature_matrix = np.array([[1,2,3,4],
                           [5,6,7,8],
                           [9,10,11,12],
                           [13,14,15,16]
                           ])
print("Original Matrix:\n",feature_matrix)
print("feature matrix[1]",feature_matrix[1])
print("feature matrix[1,2]",feature_matrix[1,2])
print("feature matrix[:1]",feature_matrix[:1])
print("feature matrix[:2]\n",feature_matrix[:2])
print("feature matrix[1:3]\n",feature_matrix[1:3])

print("feature matrix[:,:2]\n",feature_matrix[:,:2])
print("feature matrix[:,1:2]\n",feature_matrix[:,1:2])
print("feature matrix[1:3,1:3]\n",feature_matrix[1:3,1:3])




print('-'*50)









