import unittest
from heaps import max_heapify, exchange


# To implement a priority queue, we can use a max-heap or min-heap as the underlying data structure.
# Priority Queues have a lot real-world application, for example:
# We can use max-priority queue to schedule jobs on a computer.
# The max-priority queue keeps track of the jobs to be performed and their relative priorities.
# When a job is finished or interrupted, the scheduler selects the highest-priority job from among those pending by calling EXTRACT-MAX.
# The scheduler can add a new job to the queue at any time by calling INSERT.

class MaxPriorityQueue:
    """ A heap can support any priority-queue operation on a set of size n elements, in O(logn) time"""

    def __init__(self):
        """
        A: Array representation of a binary max-heap
        """
        self.A = []

    def __repr__(self) -> list:
        return self.A

    @property
    def heap_size(self) -> int:
        return len(self.A)

    # Time complexity: O(logn) -
    def insert(self, key: int) -> None:
        """
        The procedure first expands the max-heap by adding to the tree a new leaf (last-index) whose key is -infinity.
        Then call increase-key to the set the key of this new node to its correct value to maintain the heap-property.
        "Swim" the new node UPWARDS towards the root.

        :param key: Key we want to insert into the max-heap.
        """
        self.A.append(float("-inf"))
        self.increase_key(i=self.heap_size - 1, key=key)

    # Time complexity: O(logn) - Worst case we propagate a leaf node up k levels up to the root
    def increase_key(self, i: int, key: int) -> None:
        """
        Increases a key that already exists in the heap. To maintain the max-heap property, we must do the following:

        1. Update the index to new the key.
        2. Compare the key with its parent and exchange their keys if the parent is smaller. Repeat this process until
        the max-heap property holds.

        In other words, traverse UPWARDS towards the root from the given index, repeatedly comparing and exchanging with
        the parent node, continuing up this path if the key is larger than its parent.

        :param i: An index i into the array identifies the priority-queue element whose key we wish to increase
        :param key: Key we want to increase
        """
        if key < self.A[i]:
            raise Exception("New key is smaller than current key")
        self.A[i] = key

        # Check if the keys parent is smaller
        while i > 0 and self.A[(i - 1) // 2] < self.A[i]:
            parent = (i - 1) // 2
            exchange(A=self.A, i=i, j=parent)
            i = parent

    # Time complexity: O(1)
    def maximum(self) -> int:
        """ Return the root node (The biggest element in the HEAP) """
        return self.A[0]

    # Time complexity: O(logn) - It performs a constant amount of work on top of the O(logn) max-heapify algorithm
    def extract_max(self) -> int:
        """
        Performs the deletion procedure of a heap. Removes the root node from the heap, and removes the last element
        in the heap and places it as the new root node. 'Sink' the new root element DOWN by performing max-heapify on it,
        to maintain the max-heap invariant. Return the original max root node.

        Note: Deleting elements from a heap will result in a sorted array.
        """
        if len(self.A) < 1:
            raise Exception("Heap Underflow")

        max_ = self.A[0]
        self.A[0] = self.A[self.heap_size - 1]  # Set the last element in the heap to the new root node
        self.A.pop()  # Remove the last element, since we just placed it as the new root
        max_heapify(A=self.A, i=0, n=self.heap_size - 1)

        return max_


class TestMaxPriorityQueue(unittest.TestCase):
    def test_insert(self):
        queue = MaxPriorityQueue()
        queue.insert(5)
        queue.insert(10)
        queue.insert(20)
        self.assertEqual(queue.A, [20, 5, 10])

    def test_extract_max(self):
        queue = MaxPriorityQueue()
        queue.insert(5)
        queue.insert(10)
        queue.insert(200)
        queue.insert(1000)
        self.assertEqual(queue.extract_max(), 1000)

    def test_increase_key(self):
        queue = MaxPriorityQueue()
        queue.insert(1)
        queue.insert(2)
        queue.insert(3)
        queue.insert(4)

        queue.increase_key(i=3, key=1000)
        self.assertEqual(queue.maximum(), 1000)

    def test_maximum(self):
        queue = MaxPriorityQueue()
        queue.insert(1000)
        queue.insert(3000)
        queue.insert(2000)
        queue.insert(2500)
        self.assertEqual(queue.maximum(), 3000)


if __name__ == "__main__":
    unittest.main()
