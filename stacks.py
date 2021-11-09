import unittest
from typing import Any


class _Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None


# Stacks are LIFO (Last-In-First-Out)
# Applications of a stack: (Redo/Undo buttons in text editors, forward/backward buttons in a browser, tree traversals)
# We can implement a stack using a resizing array or a linked list as the underlying data structure.
# CLRS impl.
class StackArr:
    def __init__(self):
        self._data = []

    def __repr__(self) -> str:
        return str(self._data)

    # O(1)
    @property
    def peek(self) -> Any:
        return self._data[-1]

    # O(1) - Using a fixed stack size, a push would result in a stack overflow error if stack is full
    def push(self, item: Any) -> None:
        self._data.append(item)

    # O(1)
    def pop(self) -> Any:
        if self.is_empty():
            raise Exception("Stack Underflow")
        return self._data.pop()

    # O(1)
    def is_empty(self) -> bool:
        return len(self._data) == 0


# Singly LinkedList Stack Impl.
class StackLL:
    def __init__(self):
        self._head = None

    def push(self, item: Any) -> None:
        """ Push the node to the head of the linked list, this will be the top of the stack """
        new_node = _Node(item)
        new_node.next = self._head
        self._head = new_node

    @property
    def peek(self) -> Any:
        return self._head.data

    def pop(self) -> Any:
        if self._head is None:
            raise Exception("Stack Underflow")
        top = self._head
        self._head = self._head.next
        return top.data

    def is_empty(self) -> bool:
        return self._head is None


from collections import deque


# Implement a stack using a queue
class StackQ:
    def __init__(self, size=None):
        self._queue = deque()
        self._size = 0

    def push(self, item: Any) -> None:
        self._size += 1
        self._queue.append(item)  # Enqueue

    def pop(self) -> Any:
        if len(self._queue) == 0:
            raise Exception("Stack Underflow")

        # Dequeue n-1 times and enqueue the item back into end of the queue
        # After this is done, the head of the queue will be the top of the stack
        for _ in range(self._size - 1):
            self._queue.append(self._queue.popleft())

        self._size -= 1
        return self._queue.popleft()  # Use popleft to simulate a standard dequeue operation from a queue


class Test(unittest.TestCase):
    def _stack_test(self, stack_impl):
        s = stack_impl()
        s.push(7)
        s.push(0)
        s.push(3)
        self.assertEqual(s.pop(), 3)
        self.assertEqual(s.pop(), 0)
        self.assertEqual(s.pop(), 7)

        with self.assertRaises(Exception) as ctx:
            s.pop()
            self.assertTrue('Stack Underflow') in ctx.exception

    def test_stack(self):
        self._stack_test(stack_impl=StackArr)
        self._stack_test(stack_impl=StackLL)
        self._stack_test(stack_impl=StackQ)


if __name__ == "__main__":
    unittest.main()
