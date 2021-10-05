import unittest
from typing import List

Matrix = List[List[int]]


# Naive iterative solution
# Time Complexity: O(N^3) | Space Complexity: O(N^3)
def matrix_multiplication_iterative(A: Matrix, B: Matrix, n: int) -> Matrix:
    """ Let C be a new NxN matrix, multiply A by B using the dot product of rows/cols """
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


# We can solve this recursively by applying divide and conquer
# Assume n is an exact power of 2
# This assumption allows use to break our original nxn matrix into smaller blocks of size n/2
# This process is called "block partitioning"

# 1. (DIVIDE STEP) - Partition each matrix A,B and C into four (n/2 * n/2) sub matrices

# 2. (CONQUER STEP) - Recursively compute the multiplications of the sub matrices and add them together
#   - For multiplying two NxN matrices, we make 8 recursive calls, each on a matrix/subproblem of size n/2 * n/2
#   - Each recursive call multiples two n/2 * n/2 matrices which are then added together.

# 3. (COMBINE STEP) - Add the two sub matrices that were multiplied on each recursive call
#   - Each Addition till take O(N^2/4), which is O(N^2)

# Recurrence Relation = 8T(n/2) + O(n^2)
# Time Complexity: O(N^3) - Same as iterative version! With more space utilized because of the recursive call-stack
def matrix_multiplication_recursive(A: Matrix, B: Matrix, n: int) -> Matrix:
    # Base case: Matrices are 1x1
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    else:
        # Partition A into four sub matrices of size (n/2 * n/2)
        A11 = [[col for col in row[:int(len(row) / 2)]] for row in A[:int(len(A) / 2)]]
        A12 = [[col for col in row[int(len(row) / 2):]] for row in A[:int(len(A) / 2)]]
        A21 = [[col for col in row[:int(len(row) / 2)]] for row in A[int(len(A) / 2):]]
        A22 = [[col for col in row[int(len(row) / 2):]] for row in A[int(len(A) / 2):]]

        # Partition B into four sub matrices of size (n/2 * n/2)
        B11 = [[col for col in row[:int(len(row) / 2)]] for row in B[:int(len(B) / 2)]]
        B12 = [[col for col in row[int(len(row) / 2):]] for row in B[:int(len(B) / 2)]]
        B21 = [[col for col in row[:int(len(row) / 2)]] for row in B[int(len(B) / 2):]]
        B22 = [[col for col in row[int(len(row) / 2):]] for row in B[int(len(B) / 2):]]

        # Recursively compute the multiplication for all 8 sub matrices
        A11_B11 = matrix_multiplication_recursive(A11, B11, n / 2)
        A12_B21 = matrix_multiplication_recursive(A12, B21, n / 2)
        A11_B12 = matrix_multiplication_recursive(A11, B12, n / 2)
        A12_B22 = matrix_multiplication_recursive(A12, B22, n / 2)

        A21_B11 = matrix_multiplication_recursive(A21, B11, n / 2)
        A22_B21 = matrix_multiplication_recursive(A22, B21, n / 2)
        A21_B12 = matrix_multiplication_recursive(A21, B12, n / 2)
        A22_B22 = matrix_multiplication_recursive(A22, B22, n / 2)

        # Add the the two multiplied sub-matrices for each quadrant in C
        C11 = add_matrices(A11_B11, A12_B21)
        C12 = add_matrices(A11_B12, A12_B22)
        C21 = add_matrices(A21_B11, A22_B21)
        C22 = add_matrices(A21_B12, A22_B22)

        C = [[C11, C12], [C21, C22]]

        return C


# Time Complexity: O(N^2) | Space Complexity: O(N^2)
def add_matrices(A: Matrix, B: Matrix) -> Matrix:
    """ Let C be a new NxN matrix, result of adding Matrix A + Matrix B"""
    n = len(A)
    C = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] += A[i][j] + B[i][j]
    return C


class Test(unittest.TestCase):
    def test_matrix_multiplication(self):
        A = [[1, 2], [3, 4]]
        B = [[5, 6], [7, 8]]
        expected = [[19, 22], [43, 50]]

        # self.assertEqual(matrix_multiplication_iterative(A=A, B=B, n=2), expected)
        self.assertEqual(matrix_multiplication_recursive(A=A, B=B, n=2), expected)


if __name__ == "__main__":
    unittest.main()
