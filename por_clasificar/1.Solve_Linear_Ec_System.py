# Solve Linear Ec System
import numpy as np

A = np.array([[2,3],[1,2]])
b = np.array([[6,2]]).T

Sol = np.linalg.solve(A,b)
print('The solution is:\n',Sol)
