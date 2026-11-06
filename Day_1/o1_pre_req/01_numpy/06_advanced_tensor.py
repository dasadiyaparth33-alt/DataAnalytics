import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

mat_mul = np.einsum('ij,jk->ik',A,B)
print("Matrix A:\n",A)
print("Matrix B:\n",B)
print("Matrix Multiplication:\n",mat_mul)
print("-"*50)

transpos_eisum = np.einsum('ij->ji',A)
print("\nEinsum Transpose:\n",transpos_eisum)

trace_einum = np.einsum('ii->',A)
print("\nEinsum Trace:\n",trace_einum)
print("\nTrace of a Matrix:\n",np.trace(A))
