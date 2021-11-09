import unittest


# Quick sort steps:
# 1. Shuffle array - Randomize array to avoid worst-case where time is o(n^2)
# 2. Partition the array so that for some 'j'
#       - larger keys are to the right of j
#       - smaller keys are to the left of j
# 3. Recursively apply quick sort on left sub array (p...q-1) and on right sub array (q+1...r)

# Time Complexity: O(nlogn) | Space O(logn) Recursive call stack takes up space!
def quick_sort(A: list, p: int, r: int) -> None:
    # If the two pointers haven't crossed, apply quick sort.
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, r)


# O(N) Time
def partition(A: list, p: int, r: int) -> int:
    pivot = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] <= pivot:
            i = i + 1
            exchange(A, i, j)
    exchange(A, i + 1, r)
    return i + 1


def exchange(A: list, i: int, j: int) -> None:
    """ Exchange A[i] with A[j] """
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp


class Test(unittest.TestCase):
    def test_quick_sort(self):
        t1, t2 = [8, 7, 1, 5], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

        quick_sort(A=t1, p=0, r=len(t1) - 1)
        quick_sort(A=t2, p=0, r=len(t2) - 1)

        self.assertEqual(t1, [1, 5, 7, 8])
        self.assertEqual(t2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == "__main__":
    unittest.main()
