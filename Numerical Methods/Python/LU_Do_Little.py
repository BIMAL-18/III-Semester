# Write a Python program for Doolittle LU Decomposition

import numpy as np

def doolittle_decomposition():
    n = int(input("Enter Dimension of Matrix: "))
    
    a = np.zeros((n, n))
    l = np.zeros((n, n))
    u = np.zeros((n, n))

    print("Enter Elements of the Matrix:")
    for i in range(n):
        for j in range(n):
            a[i][j] = float(input(f"a[{i+1}][{j+1}]: "))

    # Initializing L and U
    for j in range(n):
        u[0][j] = a[0][j]
    for i in range(n):
        l[i][0] = a[i][0] / u[0][0]
    for i in range(n):
        l[i][i] = 1

    # Performing Doolittle LU Decomposition
    for j in range(1, n):
        for i in range(j, n):
            sum_ = sum(l[i][k] * u[k][j] for k in range(j))
            u[j][i] = a[j][i] - sum_

        for i in range(j+1, n):
            sum_ = sum(l[i][k] * u[k][j] for k in range(j))
            l[i][j] = (a[i][j] - sum_) / u[j][j]

    # Printing L and U matrices
    print("\nL Matrix:")
    print(np.array_str(l, precision=6, suppress_small=True))
    
    print("\nU Matrix:")
    print(np.array_str(u, precision=6, suppress_small=True))

doolittle_decomposition()
