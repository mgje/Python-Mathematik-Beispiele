from numpy import matrix
from numpy import linalg
A = matrix( [[1,2,3],[11,12,13],[21,22,23]]) # Creates a matrix.
x = matrix( [[1],[2],[3]] )                  # Creates a matrix (like a column vector).
y = matrix( [[1,2,3]] )                      # Creates a matrix (like a row vector).
A_inv = linalg.inv(A)	                       # invert matrix
print A_inv
print A.T                                    # Transpose of A.
print A*x                                    # Matrix multiplication of A and x.
print A.I                                    # Inverse of A.
print linalg.solve(A, x)     # Solve the linear equation system.