import unittest


# Time: O(N) - Space: O(1)
def one_away(s1: str, s2: str) -> bool:
    """ Given two strings, write a function to check if they are one edit (or zero edits) away."""

    # If the strings are equal, we know we can be one replacement away
    if len(s1) == len(s2):
        return one_edit_replace(s1, s2)
    # If we're one character away, we can potentially insert/delete
    elif len(s1) + 1 == len(s2):
        return one_edit_insert(s1, s2)
    # Same case as above but reversed
    elif len(s1) - 1 == len(s2):
        return one_edit_insert(s2, s1)

    # If the length isn't one char away or not equal, we know it can't be one edit away
    return False


def one_edit_replace(s1: str, s2: str) -> bool:
    edited = False
    n = len(s1)

    for i in range(n):
        if s1[i] != s2[i]:
            if edited:
                return False
            edited = True
    return True


# Since insertion/deletion are inverse operations, this will account for both.
def one_edit_insert(s1: str, s2: str) -> bool:
    edited = False
    i, j = 0, 0

    # Iterate over both strings and compare chars, if the chars arent equal, shift the larger string pointer over by 1
    # After one shift, all subsequent chars must be equal to be one edit away
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True


class Test(unittest.TestCase):
    def test_one_away(self):
        self.assertTrue(one_away("pale", "ple"))
        self.assertTrue(one_away("pales", "pale"))
        self.assertTrue(one_away("pale", "bale"))
        self.assertFalse(one_away("pale", "bake"))
        self.assertFalse(one_away("palel", "paze"))


if __name__ == "__main__":
    unittest.main()
