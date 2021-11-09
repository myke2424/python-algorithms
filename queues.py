import unittest
from typing import Any
from stacks import StackLL


class _Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None


# Can be implemented using an array or linked list
class QueueArr:
    def __init__(self, size: int):
        self.data = [None] * size
        self._head = 0
        self._tail = 0
        self._size = 0
        self._capacity = size

    @property
    def first(self) -> Any:
        return self.data[self._head]

    @property
    def size(self) -> int:
        return self._size

    # O(1)
    def enqueue(self, item: Any) -> None:
        if self.size == self._capacity:
            raise Exception("Queue Overflow")

        self._size += 1
        self.data[self._tail] = item
        self._tail += 1

    # O(1)
    def dequeue(self) -> Any:
        if self.is_empty():
            raise Exception("Queue Underflows")
        self._size -= 1
        item = self.data[self._head]
        self._head += 1
        return item

    # O(1)
    def is_empty(self) -> bool:
        return self._size == 0


# Using Singly-Linked List
class QueueLL:
    def __init__(self, size=None):
        self._head = None
        self._tail = None
        self._size = 0

    @property
    def size(self):
        return self._size

    @property
    def first(self):
        return self._head.data

    def enqueue(self, item: Any) -> None:
        self._size += 1
        new_node = _Node(data=item)

        if self._size == 1:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

    def dequeue(self) -> Any:
        if self._size == 0:
            raise Exception("Queue Underflows")

        self._size -= 1
        item = self._head
        self._head = self._head.next
        return item.data

    def is_empty(self) -> bool:
        return self._head is None


# Implement a queue using two stacks
class QueueTwoStacks:
    def __init__(self, size=None):
        self.stack_one = StackLL()  # Used for enqueue
        self.stack_two = StackLL()  # Used for dequeue

    def enqueue(self, item: Any) -> None:
        self.stack_one.push(item)

    def dequeue(self) -> Any:
        if self.stack_one.is_empty() and self.stack_two.is_empty():
            raise Exception("Stack Underflow")

        # We'll reverse the stack by popping each element and pushing it into the second stack, yielding a FIFO queue order.
        if self.stack_two.is_empty():
            while not self.stack_one.is_empty():
                self.stack_two.push(self.stack_one.pop())

        return self.stack_two.pop()

    def is_empty(self) -> bool:
        return self.stack_one.is_empty() and self.stack_two.is_empty()


class Test(unittest.TestCase):
    def _queue_test(self, queue_impl):
        q = queue_impl(size=10)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)

        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 3)
        q.enqueue(4)
        self.assertEqual(q.dequeue(), 4)
        self.assertEqual(q.is_empty(), True)

    def test_queue(self):
        self._queue_test(queue_impl=QueueArr)
        self._queue_test(queue_impl=QueueLL)
        self._queue_test(queue_impl=QueueTwoStacks)


if __name__ == "__main__":
    unittest.main()
