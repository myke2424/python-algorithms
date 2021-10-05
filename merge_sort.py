import unittest


# Merge sort steps:
# 1. Divide array into two halves - A[p...q] and A[q+1...r] (p = starting point ) (q = mid point) (r = end point)
# 2. Recursively sort each half
# 3. Merge two sub-arrays to produce a single sorted sub-array - A[p...r] using Merge(A,p,q,r)

# The recursion "bottoms out" when the array to be sorted has a length of 1, because every array of length 1 is already sorted.
# Time complexity: O(nlogn) - Space: O(N)
def merge_sort(A: list, p: int, r: int) -> None:
    """ CLRS Implementation """
    # If the left and right pointers haven't crossed, keep merging!
    if p < r:
        q = int((p + r) / 2)  # Mid point (use floor)
        merge_sort(A, p, q)  # Left subarray
        merge_sort(A, q + 1, r)  # Right subarray
        merge(A, p, q, r)


# Time Complexity: O(N) - Space: O(N)
def merge(A: list, p: int, q: int, r: int) -> None:
    # Use two auxillary arrays for the left and right subarrays
    n1 = q - p + 1  # length of left subarray
    n2 = r - q  # length of right subarray

    left = [0] * n1
    right = [0] * n2

    # To avoid having to check whether an array is exhausted, add an infinity value to each of both sub-arrays.
    # We know if we compare a value to the infinity index, that sub-array is exhausted.
    left.append(float("inf"))
    right.append(float("inf"))

    # Copy left half of array
    for i in range(n1):
        left[i] = A[p + i]

    # Copy right half of array
    for j in range(n2):
        right[j] = A[q + 1 + j]

    i = 0
    j = 0

    # Iterate over all indicies in the both sub-arrays and compare which values are smaller and set the smaller value in the main array
    # Remember the arrays are already sorted arrays
    # (r+1) because python is inclusive-exclusive range
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1


class Test(unittest.TestCase):
    def test_merge_sort(self):
        t1, t2 = [8, 7, 1, 5], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

        merge_sort(A=t1, p=0, r=len(t1) - 1)
        merge_sort(A=t2, p=0, r=len(t2) - 1)

        self.assertEqual(t1, [1, 5, 7, 8])
        self.assertEqual(t2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == "__main__":
    unittest.main()
