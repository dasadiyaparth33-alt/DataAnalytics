'''

'''
# Create a virtual envieronment
# python -m venv cdacvenv
# activate the virtual environment :~/cdacvenv/Scripts/activate.ps1
# pip install numpy

import numpy as np
import sys
import pip

print(sys.version)
print(np.__version__)
print(python_version := sys.version_info)
print("pip version: ",sys.modules['pip'].__version__)
print('_'*60)
vector_1d = np.array([10,20,30,40,50])
matrix_2d = np.array([[10,20,30,40],[50,60,70,80]])

print("1D Vector: ",vector_1d)
print("2D Matrix: ",matrix_2d)
print('_'*60)


#Memory footprint comparison
size = 10000
python_list = list(range(size))
numpy_array = np.arange(size)
actual_size = sys.getsizeof(python_list) + sum(sys.getsizeof(item) for item in python_list)#it's called generator expression

print("Python List Size: ",actual_size)
print("Numppy Array size: ",numpy_array.nbytes)

# numpy tensor initialization
# tensor factory function

zero_matrix = np.zeros((3,4))
one_matrix = np.ones((2,3))
constant_matrix = np.full((2,3),5)
ident_matrix = np.eye(2)

random_rang = np.random.default_rng(seed=42)
random_matrix = random_rang.random((2,3))

print("Zero Matrix:\n", zero_matrix)
print("One Matrix:\n", one_matrix)
print("Constant Matrix:\n", constant_matrix)
print("Identity Matrix:\n", ident_matrix)
