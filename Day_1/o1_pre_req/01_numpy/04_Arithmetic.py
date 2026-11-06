import numpy as np

x = np.array([[1.0,2.0],[3.0,4.0]], dtype=np.float64)
y = np.array([[5.0,6.0],[7.0,8.0]], dtype=np.float64)

print("Matrix x:\n", x)
print("Matrix y:\n", y)

print("\n== Addition ==")
print("Operator(+):\n",x+y)
print("Ans:\n ",np.add(x,y))


print("\n== Element wise Multiplication ==")
print("Operator(*):\n",x*y)
print("Ans:\n ",np.multiply(x,y))


print("\n== Division & Square Root ==")
print("division of Two Elements:\n",x/y)
print("division of Two Elements:\n",np.divide(x,y))

print("Element wise square root:\n ",np.sqrt(x,y))

print("-"*50)


raw_signals = np.array([-1.7, -0.2, 0.5, 1.4, 2.8])
print("Raw Signals:",raw_signals)
print("Floor: ",np.floor(raw_signals))
print("Ceil: ",np.ceil(raw_signals))
print("Round: ",np.round(raw_signals))
print("-"*50)
print("Ceil of 2.4: ",np.ceil(2.4))
print("Floor of 2.4: ",np.floor(2.4))
print("Ceil of -2.4: ",np.ceil(-2.4))
print("Floor of -2.4: ",np.floor(-2.4))
print("-"*50)

dataset = np.array([[10,20,30],
                    [40,50,60],
                    [70,80,90]  
                    ])

print("Dataset:\n",dataset)
#Global Reduction
print("Sum of all elements: ",np.sum(dataset))
print("Mean of all elements: ",np.mean(dataset))

print("-"*50)

# axis = 0 means column wise operation
print("Sum of all elements column wise: ",np.sum(dataset, axis=0))
print("Mean of all elements column wise: ",np.mean(dataset, axis=0))
# axis = 1 means row wise operation
print("Sum of all elements row wise: ",np.sum(dataset, axis=1))
print("Mean of all elements row wise: ",np.mean(dataset, axis=1))

print("-"*50)

raw_features = np.array([[1.0,2.0,3.0],
                            [4.0,5.0,6.0],
                            [7.0,8.0,9.0]
                            ])

col_means = np.mean(raw_features, axis=0)
col_std = np.std(raw_features, axis=0)
'''
formula for standar deviation is
standard_deviation = sqrt(sum((x-mean)^2)/N)
step 1: find mean of each column
step 2: find the difference of each element from mean
step 3: square the differences
step 4: sum the squared differences
step 5: divide by the number of elements
step 6: take the square root
'''
#compute standardized feature using brosadcasting (z-score normalization)
standardized_features = (raw_features - col_means) / col_std

print("Raw Features:\n",raw_features)
print("Column Means: ",np.round(col_means, 2))
print("Column Standard Deviations: ",np.round(col_std, 2))
print("Standardized Features:\n",np.round(standardized_features,3))

print("-"*50)
