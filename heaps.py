import unittest


# A Heap is a complete binary tree that's represented using an array
# Instead of traversing a tree, we can access nodes by using simple math applied to the indices
# The following "formula" is how we'll access parent/child nodes in the heap

# If a node is at A[i]
# Its left child is at A[2*i] (This assumes array indices start 1)
# Its right child is at A[(2*i) + 1] (This assumes array indices start 1)
# Its parent is at Index A[floor(i/2)]

# Since python has 0 based arrays, the formula will be as follows:
# Left child = A[(2*i) + 1]
# Right child = A[(2*i) + 2]
# Parent = A[floor((i-1)/2)]

# Key properties of a heap
# - Max-Heap: A[parent(i)] >= A[i]  -> Root Node will be biggest element
# - Min-Heap: A[parent(i)] <= A[i]  -> Root Node will be smallest element
# - Height of a heap = O(logn), where each level has 2^k nodes
# - Max-Heap or Min-Heap is a good way to implement a Priority Queue

# === CLRS Implementation of Heap Algorithms  ===

# In general a given node could propagate k levels down the tree, k = logn
# Time complexity: O(logn) | Space complexity: O(1)
def max_heapify(A: list, i: int, n: int) -> None:
    """
    Algorithm used to maintain the max heap property for the given index.
    This will use the same procedure as "heap deletion" where it keeps moving the element DOWN, exchanging
    with the larger child until it finds it spot in the heap.

    :param A: Array
    :param i: Array Index to perform max_heapify on
    :param n: Number of Nodes (indices) in the Heap
    """
    # At each index i, we are finding the largest key among the current node, left child and right child.
    left_child = (2 * i) + 1
    right_child = (2 * i) + 2

    if left_child <= n and A[left_child] > A[i]:
        largest = left_child
    else:
        largest = i

    if right_child <= n and A[right_child] > A[largest]:
        largest = right_child

    # If a child node is greater than A[i], exchange it and make a recursive-call
    # This way, the index will find its spot in the heap and maintain the max-heap invariant
    if largest != i:
        exchange(A=A, i=i, j=largest)
        max_heapify(A=A, i=largest, n=n)


# T(n) = (n/2)*logn = n*logn (n/2 = n in terms of asymptotic bounds)
# N number of times performing logn calculations = O(nlogn)
# Time complexity: (nlogn) | Space: O(1)
def build_max_heap(A: list, n: int) -> None:
    """
    Create a max-heap from an unsorted array.

    The leaf nodes of the heap already satisfy the max-heap invariant (they don't have children to compare against),
    that's why we'll start our iteration at floor(n/2). We'll iterate from right-to-left, skipping all leaf nodes.
    We'll run max_heapify on all indices from i=n/2 to i=0.

    :param A: Array
    :param n: Number of Nodes (indices) in the Heap:
    """
    # NOTE: "//" is floor division in python
    # Start at i = floor(n/2), up until index 0 (inclusive-exclusive range)
    for i in range(n // 2, -1, -1):
        max_heapify(A=A, i=i, n=n)


# T(N) = 2(nlogn) = nlogn
# Time Complexity: O(nlogn) | Space: O(1)
def heap_sort(A: list, n: int) -> None:
    """
    Heap Sort sorts an unsorted array following 2 steps:

    1. Build a max-heap from the unsorted array
    2. Iterating the array right-to-left, exchange the last node in the current heap (A[i]) with the root node (A[0]),
    then call max_heapify on the new root to maintain the max-heap invariant (push the node down until it finds its spot in the heap).
    Each call to max_heapify will have i-1 # of nodes, where the i'th node (old root that was exchanged) will be in its sorted position in the array.

    :param A: Array
    :param n: Number of Nodes (indices) in the Heap
    """
    build_max_heap(A=A, n=n)
    for i in range(n, 0, -1):
        exchange(A, 0, i)
        max_heapify(A, 0, i - 1)


# Below is the Min-Heap implementation, it uses the same algorithm as Max-Heap,
# except the parent node is always smaller than its children. The root node is the smallest element in the heap.

def min_heapify(A: int, i: int, n: int) -> None:
    """
    Same algorithm as max_heapify, except at each index I,
    we're finding the SMALLEST key among the current node, left child and right child.
    The only thing that changes is our comparison checks
    """
    left_child = (2 * i) + 1
    right_child = (2 * i) + 2

    if left_child <= n and A[left_child] < A[i]:
        smallest = left_child
    else:
        smallest = i

    if right_child <= n and A[right_child] < A[smallest]:
        smallest = right_child

    if smallest != i:
        exchange(A=A, i=i, j=smallest)
        min_heapify(A=A, i=smallest, n=n)


def build_min_heap(A: list, n: int) -> None:
    for i in range(n // 2, -1, -1):
        min_heapify(A=A, i=i, n=n)


def heap_sort_reverse(A: list, n: int) -> None:
    """ To sort an array in reverse order (Largest-to-Smallest), use a min_heap instead of a max_heap """
    build_min_heap(A=A, n=n)
    for i in range(n, 0, -1):
        exchange(A, 0, i)
        min_heapify(A, 0, i - 1)


def exchange(A: list, i: int, j: int) -> None:
    """ Exchange A[i] with A[j] """
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp


class MaxHeapTest(unittest.TestCase):
    def test_max_heapify(self):
        a1 = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        a1_expected = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        max_heapify(A=a1, i=0, n=len(a1) - 1)
        self.assertEqual(a1, a1_expected)

        a2 = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        a2_expected = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        max_heapify(A=a2, i=1, n=len(a2) - 1)
        self.assertEqual(a2, a2_expected)

        a3 = [16, 4, 10, 14, 7, 11, 3, 2, 8, 1]
        a3_expected = [16, 4, 11, 14, 7, 10, 3, 2, 8, 1]
        max_heapify(A=a3, i=2, n=len(a3) - 1)
        self.assertEqual(a3, a3_expected)

    def test_build_max_heap(self):
        a1 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        a1_expected = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        build_max_heap(A=a1, n=len(a1) - 1)
        self.assertEqual(a1, a1_expected)

        a2 = [2, 8, 5, 3, 9, 1]
        a2_expected = [9, 8, 5, 3, 2, 1]
        build_max_heap(A=a2, n=len(a2) - 1)
        self.assertEqual(a2, a2_expected)

    def test_heap_sort(self):
        a1 = [7, 4, 3, 1, 2]
        a1_expected = [1, 2, 3, 4, 7]
        heap_sort(A=a1, n=len(a1) - 1)
        self.assertEqual(a1, a1_expected)

        a2 = [1, 5, 3, 8, 7, 6]
        a2_expected = [1, 3, 5, 6, 7, 8]
        heap_sort(A=a2, n=len(a2) - 1)
        self.assertEqual(a2, a2_expected)


class MinHeapTest(unittest.TestCase):
    def test_min_heapify(self):
        a1 = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        a1_expected = [4, 7, 10, 14, 1, 9, 3, 2, 8, 16]
        min_heapify(A=a1, i=0, n=len(a1) - 1)
        self.assertEqual(a1, a1_expected)

        a2 = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        a2_expected = [16, 4, 10, 14, 7, 9, 3, 2, 8, 1]
        min_heapify(A=a2, i=1, n=len(a2) - 1)
        self.assertEqual(a2, a2_expected)

        a3 = [16, 4, 10, 14, 7, 11, 3, 2, 8, 1]
        a3_expected = [16, 4, 3, 14, 7, 11, 10, 2, 8, 1]
        min_heapify(A=a3, i=2, n=len(a3) - 1)
        self.assertEqual(a3, a3_expected)

    def test_build_min_heap(self):
        a1 = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
        a1_expected = [1, 2, 3, 4, 7, 9, 10, 14, 8, 16]
        build_min_heap(A=a1, n=len(a1) - 1)
        self.assertEqual(a1, a1_expected)

        a2 = [2, 8, 5, 3, 9, 1]
        a2_expected = [1, 3, 2, 8, 9, 5]
        build_min_heap(A=a2, n=len(a2) - 1)
        self.assertEqual(a2, a2_expected)

    def test_heap_sort_reverse(self):
        a1 = [1, 4, 5, 7, 2]
        a1_expected = [7, 5, 4, 2, 1]
        heap_sort_reverse(A=a1, n=len(a1) - 1)
        self.assertEqual(a1, a1_expected)

        a2 = [1, 5, 3, 8, 7, 6]
        a2_expected = [8, 7, 6, 5, 3, 1]
        heap_sort_reverse(A=a2, n=len(a2) - 1)
        self.assertEqual(a2, a2_expected)


if __name__ == "__main__":
    unittest.main()
