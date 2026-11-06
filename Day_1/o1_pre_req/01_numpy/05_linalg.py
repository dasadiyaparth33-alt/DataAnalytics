import numpy as np

vector_a = np.array([9,10])
vector_b = np.array([11,12])

print("Vector a:\n", vector_a)
print("Vector b:\n", vector_b)
print("\n== Dot Product ==")
print("Dot product (operator): ", np.dot(vector_a, vector_b))
print("Dot product (method): ", np.inner(vector_a, vector_b))

# operator @ is used for matrix multiplication in python 3.5 and above
print("Operator (@): ", vector_a @ vector_b)

print("-"*50)

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

print("Matrix x:\n", x)
print("Matrix y:\n", y)
print("\nElement wise product :\n",x*y)

print("\n== matrix Multiplication== ")
print("Operator np.dot:\n",np.dot(x,y))
print("Operator @:\n",x@y)


print("-"*50)

matrix_data = np.array([[1,2,3],[4,5,6],[7,8,9]])

row_vector = np.array([10,20,30])
row_brodcaster = matrix_data + row_vector
print(" Row Vector Brodcast Result:\n",row_brodcaster)

print("-"*50)

col_vector = np.array([[100],[200],[300]])
col_brodcaster = matrix_data + col_vector
print(" Column Vector Brodcast Result:\n",col_brodcaster)


print("-"*50)
