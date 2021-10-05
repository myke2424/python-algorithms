import unittest


# Time O(N) - Space O(N)
def URLify(s: str) -> str:
    """ Replace spaces with %20 and remove trailing spaces  """
    # Count the number of white spaces
    space_count = 0
    for char in s:
        if char == ' ':
            space_count += 1

    char_list = [None] * (len(s) + space_count * 2)  # multiply space count by 2 since replace str is 3chars
    n = len(char_list)
    orig_idx = 0
    new_idx = 0

    while new_idx < n:
        if s[orig_idx] == ' ':
            char_list[new_idx] = '%'
            char_list[new_idx + 1] = '2'
            char_list[new_idx + 2] = '0'
            new_idx += 3
        else:
            char_list[new_idx] = s[orig_idx]
            new_idx += 1

        orig_idx += 1

    return ''.join(char_list)


class Test(unittest.TestCase):
    def test_URLify(self):
        self.assertEqual(URLify("Mr John Smith"), "Mr%20John%20Smith")


if __name__ == "__main__":
    unittest.main()
