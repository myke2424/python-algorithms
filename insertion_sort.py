import unittest


# Swap a[i] with each larger entry to its left
# Scan left to right, entries to the left of the pointer are in ascending order
# Entries to the right of the pointer have not been seen
# Twice as fast as selection sort
# Time Complexity: O(N^2) | Space: O(1)
def insertion_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                tmp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = tmp
            else:
                break

    return arr


def insertion_sort_clrs(arr: list) -> list:
    n = len(arr)
    for j in range(1, n):
        key = arr[j]  # element to be compared
        i = j - 1

        # Only evaluate items to the left our key, shift items bigger than our key to the right by one index.
        # Decrement the 'i' pointer by one each iteration
        # If we find a smaller element (a[i] < key) we place our key to the right of it.
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]  # move bigger number over one index
            i -= 1
        arr[i + 1] = key

    return arr


class Test(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([8, 7, 1, 5]), [1, 5, 7, 8])
        self.assertEqual(insertion_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(insertion_sort_clrs([8, 7, 1, 5]), [1, 5, 7, 8])
        self.assertEqual(insertion_sort_clrs([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


if __name__ == "__main__":
    unittest.main()
