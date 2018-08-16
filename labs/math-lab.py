# import matplotlib.pyplot as plt
import numpy as np

# Consider the system of LINER equations
# x + y + z = 6
# 2y + 5z = -4
# 2x + 5y -z =27

# This is the same as:

# |1 1 1| |x| = |6|
# |0 2 5| |y| = |-4|
# |2 5 -1| |z| = |27|
#   A       X     B

# A*X =B
# X = B/A = B*A^-1

A = np.array([[1,1,1],[0,2,5],[2,5,-1]])
B = np.array([[6],[-4],[27]])

X = np.dot(np.linalg.inv(A),B)
print(X)



# x = np.linspace(-2,2,40)
# print(x)
# y = 2 + np.sqrt(abs(x))

# plt.plot(x,y,'ms-')
# plt.show()

