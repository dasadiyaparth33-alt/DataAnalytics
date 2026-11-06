import numpy as np

inch_mesures = np.array([1.0,2.5,3.5,5])
cm_mesures = inch_mesures * 2.54  # Vectorized Opetration

print("Inches :",inch_mesures)
print("CMS :",cm_mesures)

feature_a = np.array([1,2,3,4,5])
feature_b = np.array([10,20,30,40,50])

print('👽'*60)

print("Feature A: ",feature_a)
print("Feature B: ",feature_b)
print("Sum of Feature : ", feature_a + feature_b)
print("Difference  of Feature : ", feature_a - feature_b)
print("Product of Feature : ", feature_a * feature_b)
print("Patio of Feature : ", feature_a / feature_b)

print('👽'*60)

# Algorithm Rigor
rng = np.random.default_rng(seed=42)
signal_data = rng.uniform(low = 0.0, high = 1.0, size = (4,4))
print("Signal Data: ")
print(signal_data)

#vectorized mask
mask = signal_data > 0.7 #boolean mask for filtering values grater than 0.7
print("Mask:\n ",mask)

print("Filtered Signal Data (value > 0.7)") # Data filtering using boolean mask 
print(signal_data[mask])

print('👽'*60)

# Data type rigor
int_implicit = np.array([1,2,3,4,5]) # default datatype is int64
int_explicit = np.array([1,2,3,4,5])# default dype is int64
print("Implicit integer array: ",int_implicit," and dtype is :",int_implicit.dtype)
print("Explicit integer array: ",int_explicit," and dtype is :",int_explicit.dtype)
