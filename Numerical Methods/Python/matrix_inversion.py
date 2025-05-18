# Write a Python program for Matrix Inversion with Gauss Jordan

def matrix_inversion():
    import numpy as np
    n = int(input("Enter the dimension of the coefficient matrix: "))

    a = np.zeros((n, 2 * n))

    print("Enter the coefficient matrix:")
    for i in range(n):
        for j in range(n):
            a[i][j] = float(input(f"a[{i+1}][{j+1}]: "))

    # Augmenting the identity matrix
    for i in range(n):
        for j in range(n):
            a[i][j + n] = 1 if i == j else 0

    # Applying Gauss-Jordan Elimination
    for k in range(n):
        pivot = a[k][k]
        for j in range(2 * n):
            a[k][j] /= pivot

        for i in range(n):
            if i != k:
                term = a[i][k]
                for j in range(2 * n):
                    a[i][j] -= a[k][j] * term

    # Printing the inverse matrix
    print("\nMatrix Inverse:")
    for i in range(n):
        for j in range(n, 2 * n):
            print(f"{a[i][j]:.6f}", end="\t")
        print()

matrix_inversion()
