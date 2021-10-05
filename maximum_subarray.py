import unittest

from math import floor
from typing import Tuple


# Note: We can solve this in O(N) time and O(1) space using the Sliding Window Technique.
# This is mainly for divide & conquer practice.


# We can derive the time complexity simply using a recurrence relation and masters theorem.
# Recurrence relation = 2T(n/2) + O(N)

# Returns indices i and j such that A[i..j] has the greatest sum, along with the sum of those indices
# Time Complexity: O(nlogn) | Space Complexity: O(N) - Where N is the size of the recursive call-stack
def find_maximum_subarray(A: list, low: int, high: int) -> Tuple[int, int, int]:
    # Base case: If theirs only one element then that's the max sum.
    if high == low:
        return low, high, A[low]
    else:
        mid = floor((low + high) / 2)

        # Divide the array into two sub-arrays and find the max sum of the left and right subarray
        left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)  # T(n/2)
        right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)  # T(n/2)

        # Find max subarray that crosses the midpoint (left and right)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)  # O(N)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum


def find_max_crossing_subarray(A: int, low: int, mid: int, high: int) -> Tuple[int, int, int]:
    max_left_idx, max_right_idx = None, None

    left_sum = float("-inf")
    sum_ = 0

    # Find max subarray of the left subarray A[low...mid]
    # Go from mid-low (right to left), it's low +1 because python has a inclusive-exclusive range
    for i in range(mid, low + 1, -1):
        sum_ += A[i]
        if sum_ > left_sum:
            left_sum = sum_
            max_left_idx = i  # Keep track of the max left pointer, so we know the the starting index of the max subarr

    right_sum = float("-inf")
    sum_ = 0

    # The max subarray of the right subarray
    for j in range(mid + 1, high + 1):
        sum_ += A[j]
        if sum_ > right_sum:
            right_sum = sum_
            max_right_idx = j  # Ending index of the max subarr

    # Return the indices and the combined sum of the two sub-arrays
    return max_left_idx, max_right_idx, left_sum + right_sum


# Sliding Window Approach -> O(N) Time | O(1) Space
def find_max_subarray_sliding_window(A: list) -> int:
    max_sum = float("-inf")
    current_window_sum, window_start = 0, 0

    for window_end in range(len(A)):
        current_window_sum += A[window_end]
        max_sum = max(max_sum, current_window_sum)

        # If our current sum is negative, let's shrink our window
        while current_window_sum < 0:
            current_window_sum -= A[window_start]
            window_start += 1

    return max_sum


class Test(unittest.TestCase):
    def test_find_max_subarray(self):
        t1 = [-1, -1, 2, 3, 1, -2, -5]  # max sub-array = (2,3,1) i = 2 j = 4 -> A[2..4]
        self.assertEqual(find_maximum_subarray(A=t1, low=0, high=len(t1) - 1), (2, 4, 6))
        self.assertEqual(find_max_subarray_sliding_window(A=[-1, -1, 2, 3, 1, -2, -5]), 6)


if __name__ == "__main__":
    unittest.main()
