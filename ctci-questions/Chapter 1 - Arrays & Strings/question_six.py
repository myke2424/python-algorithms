import unittest


# Time: O(N) - Space: O(N)
def string_compression(s: str) -> str:
    """ basic string compression using the counts of repeated characters """

    # Use a char list instead of a str, since strings are immutable, concatenation results in O(N),
    # In our string iteration this would result in O(N^2)...
    compressed = []
    n = len(s)

    consecutive_count = 0

    # At each iteration, check if the current char is the same as the next,
    # if not append the current char and its consecutive count
    for i in range(n):
        consecutive_count += 1

        if (i + 1) >= n or s[i] != s[i + 1]:
            # Use append for O(1) instead of O(N) list/str concat
            compressed.append(s[i])
            compressed.append(str(consecutive_count))
            consecutive_count = 0

    return ''.join(compressed) if len(compressed) < len(s) else s


class Test(unittest.TestCase):
    def test_string_compression(self):
        self.assertEqual(string_compression("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(string_compression("abcd"), "abcd")


if __name__ == "__main__":
    unittest.main()
