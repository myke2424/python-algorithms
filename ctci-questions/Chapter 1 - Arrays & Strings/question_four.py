import unittest


# Time: O(N) - Space: O(N)
def palindrome_permutation(s: str) -> bool:
    """
    Given a string, check if it a permutation of a palindrome. A palindrome is a word phrase that
    is the same forwards and backwards
    """

    char_freq = {}

    # Remove any spaces in the string and build the frequency map
    for char in s.replace(" ", "").lower():
        freq = char_freq.get(char, 0) + 1
        char_freq[char] = freq

    # To be a permutation of a palindrome, a string can have no more than one character that is odd
    odd_chars = 0
    for freq in char_freq.values():
        if not freq % 2 == 0:
            odd_chars += 1

        if odd_chars > 1:
            return False

    return True


class Test(unittest.TestCase):
    def test_palindrome_permutation(self):
        self.assertEqual(palindrome_permutation("Tact Coa"), True)  # permutations: "taco cat", "atco cta", etc


if __name__ == "__main__":
    unittest.main()
