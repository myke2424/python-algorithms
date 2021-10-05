# Find average of all contigous subarrays of size "5" in given array
# This is a fixed size sliding window problem
def find_avg_subarray(arr: list, k: int) -> list[int]:
    current_window_sum = 0
    averages = []
    window_start = 0

    for window_end in range(len(arr)):
        current_window_sum += arr[window_end]

        # Have we grown our window to size K?
        if window_end >= k - 1:
            average = current_window_sum / ((window_end - window_start) + 1)
            averages.append(average)

            current_window_sum -= arr[window_start]
            window_start += 1

    return averages


# Given an array of positive nums and a positive number 'k', find the max sum of any contigous subarray of size k
def max_sum_subarray(arr: list, k: int) -> int:
    window_start = 0
    max_sum = float("-inf")
    current_window_sum = 0

    for window_end in range(len(arr)):
        current_window_sum += arr[window_end]

        # Has our window grown to size K?
        if window_end >= k - 1:
            # Do our sum processing
            max_sum = max(max_sum, current_window_sum)
            # Remove element going out of the window
            current_window_sum -= arr[window_start]
            window_start += 1

    return max_sum


# Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray
# whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.
def smallest_sub_array(arr: list, s: int) -> int:
    current_window_sum, window_start = 0.0, 0
    smallest_size = float("inf")

    for window_end in range(len(arr)):
        current_window_sum += arr[window_end]

        # Do our processing!
        while current_window_sum >= s:
            smallest_size = min(smallest_size, (window_end - window_start) + 1)
            # Remove the element going out of the window
            current_window_sum -= arr[window_start]
            window_start += 1

    res = smallest_size if smallest_size != float('inf') else 0

    return res


# Given a string, find the length of the longest substring in it with no more than K distinct characters
def longest_substring_distinct_chars(s: str, k: int) -> int:
    window_start, longest = 0, 0
    char_freq = {}

    for window_end in range(len(s)):
        # Set char frequency
        freq = char_freq.get(s[window_end], 0) + 1
        char_freq[s[window_end]] = freq

        # Shrink our window to have k distinct chars!
        while len(char_freq) > k:
            char_freq[s[window_start]] -= 1
            if char_freq[s[window_start]] == 0:
                del char_freq[s[window_start]]

            window_start += 1

        # Once we have k distinct chars in our freq map, do our max length processing!
        current_window_size = (window_end - window_start) + 1
        longest = max(longest, current_window_size)

    return longest


def fruits_into_baskets(fruits: list) -> int:
    window_start = 0
    max_fruits = 0
    fruit_freq = {}

    for window_end in range(len(fruits)):
        freq = fruit_freq.get(fruits[window_end], 0) + 1
        fruit_freq[fruits[window_end]] = freq

        # If we violate our 2 fruit constraint
        while len(fruit_freq) > 2:
            # Shrink our window!
            fruit_freq[fruits[window_start]] -= 1

            if fruit_freq[fruits[window_start]] == 0:
                del fruit_freq[fruits[window_start]]

            window_start += 1

        current_window_size = (window_end - window_start) + 1
        max_fruits = max(max_fruits, current_window_size)

    return max_fruits


def longest_substring_no_repeating_chars(s: str) -> int:
    window_start = 0
    longest_size = 0
    char_freq = {}

    for window_end in range(len(s)):
        freq = char_freq.get(s[window_end], 0) + 1
        char_freq[s[window_end]] = freq

        # While the current char has a frequency greater than 1, lets shrink the window!
        while char_freq[s[window_end]] > 1:
            char_freq[s[window_start]] -= 1
            if char_freq[s[window_start]] == 0:
                del char_freq[s[window_start]]
            window_start += 1

        current_window_size = (window_end - window_start) + 1
        longest_size = max(longest_size, current_window_size)

    return longest_size
