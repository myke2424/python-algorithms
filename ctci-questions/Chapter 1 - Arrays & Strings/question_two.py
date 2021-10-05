import unittest


# Time: O(N) - Space - O(N)
def check_permutation(s1: str, s2: str) -> bool:
    """ Given two strings, check if one string is a permutation of the other """
    if len(s1) != len(s2):
        return False

    s1_freq = {}
    s2_freq = {}
    n = len(s1)

    for i in range(n):
        s1_char = s1[i]
        s2_char = s2[i]

        s1_freq[s1_char] = s1_freq.get(s1_char, 0) + 1
        s2_freq[s2_char] = s2_freq.get(s2_char, 0) + 1

    for char in s1_freq.keys():
        if s1_freq.get(char) != s2_freq.get(char):
            return False

    return True


# Complexity depends on sorting algorithm, say were using QuickSort
# Time: O(nlogn) - Space: O(logn)
def check_permutation_sort(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    s1, s2 = sorted(s1), sorted(s2)

    n = len(s1)
    for i in range(n):
        if s1[i] != s2[i]:
            return False

    return True


class Test(unittest.TestCase):
    def test_check_permutation(self):
        self.assertTrue(check_permutation("abc", "bac"))
        self.assertFalse(check_permutation("m", "mike"))
        self.assertFalse(check_permutation("mike", "rain"))


if __name__ == "__main__":
    unittest.main()
