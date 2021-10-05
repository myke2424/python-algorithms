import unittest


# Time: O(N) - Space: O(N)
def is_unique(s: str) -> bool:
    """ Determine if a string has all unique chars """
    seen_chars = {}
    for char in s:
        if seen_chars.get(char) is not None:
            return False

        seen_chars[char] = True

    return True


# Assuming ASCII (128-chars)
# Time: O(N) - Space: O(1) (We won't iterate over a str greater than 128chars)
def is_unique_ascii(s: str) -> bool:
    if len(str) > 128:
        return False

    char_set = [False] * 128
    for char in s:
        val = ord(char)  # unicode val of char
        if char_set[val]:
            return False
        char_set[val] = True

    return True


class Test(unittest.TestCase):
    def test_is_unique(self):
        self.assertTrue(is_unique("mike"))
        self.assertFalse(is_unique("kinesis"))
        self.assertTrue(is_unique("m"))


if __name__ == "__main__":
    unittest.main()
