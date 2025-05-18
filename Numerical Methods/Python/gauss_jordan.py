# Write a python program for Gauss Jordan Method

def gauss_jordan():
    import numpy as np
    n = int(input("Enter the dimension of the system of equations: "))
    
    a = np.zeros((n, n+1))

    print("Enter the augmented matrix (including RHS):")
    for i in range(n):
        for j in range(n+1):
            a[i][j] = float(input(f"a[{i+1}][{j+1}]: "))

    for k in range(n):
        pivot = a[k][k]
        for j in range(n+1):
            a[k][j] /= pivot
        
        for i in range(n):
            if i != k:
                term = a[i][k]
                for j in range(n+1):
                    a[i][j] -= a[k][j] * term

    print("\nSolution:")
    for i in range(n):
        print(f"x{i+1} = {a[i][n]:.6f}")

gauss_jordan()
