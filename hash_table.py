from typing import Any, Callable, Union, Optional
from itertools import islice, cycle
import unittest


# Hash function is critical. A bad hash function could result in a lot of hash collisions yielding an O(N) search

# To resolve hash collisions, we can use 2 methods:
# 1. Probing Methods
#   - Linear Probing, Quadratic Probing, Double Hashing
# 2. Chaining (Linked Lists at each index storing all values with the same hash)

class HashTableChaining:
    """ Hash table w/ separate chaining for hash collisions """

    def __init__(self, hash_function: Callable, size: int):
        self.hash = hash_function
        self.data = [None] * size  # Resize array when it's 50% full.
        self._hash_collisions = 0

    # O(1) Avg case | O(N) when high hash collisions
    def get(self, key: Union[str, int]) -> Any:
        index = self.hash(k=key, m=len(self.data))

        if self.data[index] is None:
            return None

        return self.data[index].search(key=key)

    # O(1)
    def put(self, key: Union[str, int], value: Any) -> None:
        index = self.hash(k=key, m=len(self.data))

        if self.data[index] is None:
            self.data[index] = LinkedList()
        else:
            self._hash_collisions += 1
            curr_node = self.data[index].head

            while curr_node is not None:
                # Key already exists in the hash table, overwrite the key
                if curr_node.key == key:
                    curr_node.value = value
                    return
                curr_node = curr_node.next

        # Insert the new key/value
        self.data[index].insert(key=key, value=value)

    # O(1) Avg case - O(N) Worst case if need to traverse N nodes in the linked list
    def delete(self, key: Union[str, int]) -> None:
        index = self.hash(k=key, m=len(self.data))

        if self.data[index] is None:
            return

        linked_list = self.data[index]
        linked_list.delete(key=key)

    def clear(self) -> None:
        self.data = [None] * len(self.data)


class HashTableProbing:
    """
    Using open addressing for hash collisions
    Probing methods for hash collisions (Linear Probing/Quadratic Probing/Random Probing/Double Hashing)
    We'll use Linear Probing in Cyclically (After the last index, probe circles around at index 0)
    """

    def __init__(self, hash_function: Callable, size: int):
        self.hash = hash_function
        self.data = [None] * size
        self._hash_collisions = 0

    def _linear_probe(self, index: int, key: Union[str, int]) -> Optional[int]:
        """ Return available index from linear probing. Index=Starting Index"""
        iterations = 0
        while iterations < len(self.data):
            # Index out of bounds, circle around to index 0.
            if index == len(self.data):
                index = 0
            if self.data[index] is not None:
                k, _ = self.data[index]
                # Key already exists, so we return the index that will we overwrite
                if k == key:
                    return index
            else:
                # Index is available
                return index
            index += 1
            iterations += 1
        return None

    def get(self, key: Union[str, int]) -> Any:
        index = self.hash(k=key, m=len(self.data))

        if self.data[index] is None:
            return None

        iterations = 0
        # NOTE: Itertools.cycle() is a neat way to iterate cyclically. Isslice starts the iterator at a given index
        for item in islice(cycle(self.data), index, None):
            if iterations == len(self.data):
                break
            if item is not None:
                k, v = item
                if k == key:
                    return v
            iterations += 1
        return None

    def put(self, key: Union[str, int], value: Any) -> None:
        index = self.hash(k=key, m=len(self.data))

        if self.data[index] is None:
            self.data[index] = (key, value)
        else:
            index = self._linear_probe(index=index, key=key)
            self.data[index] = (key, value)

    def delete(self, key: Union[str, int]) -> None:
        if self.get(key) is None:
            return
        index = self.hash(k=key, m=len(self.data))

        iterations = 0
        for item in islice(cycle(self.data), index, None):
            if iterations == len(self.data):
                break
            if item is not None:
                k, v = item
                if k == key:
                    self.data[index] = None
            iterations += 1
            index += 1
        return None


class _Node:
    def __init__(self, key: Union[str, int], value: Any):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, key: Union[str, int]) -> Any:
        curr = self.head
        while curr is not None:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None

    def insert(self, key: Union[str, int], value: Any) -> None:
        new_node = _Node(key=key, value=value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key: Union[str, int]) -> None:
        curr = self.head
        prev = None

        found = False
        while curr is not None:
            if curr.key == key:
                found = True
                break
            prev = curr
            curr = curr.next

        if found:
            if prev:
                prev.next = curr.next
            else:
                self.head = self.head.next


# M represents the length of the underlying array.
def hash_division_method(k: Union[str, int], m: int) -> int:
    return hash(k) % m


def hash_division_method_two(k: Union[str, int], m: int) -> int:
    return ((2 * hash(k)) + 1) % m


class Test(unittest.TestCase):
    def _hash_table_test(self, hash_function: Callable, hash_table: object):
        ht = hash_table(hash_function=hash_function, size=10)
        ht.put(key="name", value="mike")
        ht.put(key="school", value="McMaster")
        ht.put(key="city", value="Hamilton")
        print(f"HASH COLLISIONS FOR {hash_function.__name__}: {ht._hash_collisions}")

        self.assertEqual(ht.get("name"), "mike")
        self.assertEqual(ht.get("school"), "McMaster")
        self.assertEqual(ht.get("city"), "Hamilton")
        ht.put("city", 123)
        self.assertEqual(ht.get("city"), 123)

        self.assertEqual(ht.get("agz"), None)
        self.assertEqual(ht.get("zzz"), None)
        ht.delete("name")
        self.assertEqual(ht.get("name"), None)
        ht.delete("school")
        self.assertEqual(ht.get("school"), None)
        ht.delete("city")
        self.assertEqual(ht.get("city"), None)

    def test_hash_table(self):
        self._hash_table_test(hash_function=hash_division_method, hash_table=HashTableChaining)
        self._hash_table_test(hash_function=hash_division_method_two, hash_table=HashTableChaining)
        self._hash_table_test(hash_function=hash_division_method, hash_table=HashTableProbing)


if __name__ == "__main__":
    unittest.main()
