import unittest


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None
        self.prev = None


class SinglyLinkedList:
    """ In a singly linked list we only keep references to the next node """

    def __init__(self):
        self.head = None

    def __str__(self):
        s = ""
        current = self.head
        while current is not None:
            s += f"{current.data}->"
            current = current.next

        s += "None"
        return s

    # O(N)
    def search(self, item: int) -> Node:
        """ Search for the node """
        current = self.head
        while current is not None and current.data != item:
            current = current.next

        return current

    # O(1)
    def insert(self, item: int) -> None:
        """ Insert at the head of the linked list """
        new_node = Node(data=item)
        new_node.next = self.head
        self.head = new_node

    # O(N)
    def delete(self, item: int) -> None:
        """ Delete the node """
        current = self.head
        prev = None

        if item == self.head.data:
            self.head = self.head.next
        else:
            while current is not None:
                if current.data == item:
                    prev.next = current.next
                prev = current
                current = current.next


class DoublyLinkedList:
    """
    In a double linked list, we keep reference to the previous and next node
    Search is the same as singly-linked-list. Insertion/Deletion will change due to the 'prev' pointer.
    """

    def __init__(self):
        self.head = None

    def insert(self, item: int) -> None:
        new_node = Node(item)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def search(self, item: int) -> int:
        curr = self.head
        while curr is not None and curr.data != item:
            curr = curr.next
        return curr

    def delete(self, item: int) -> None:
        if item == self.head.data:
            self.head = self.head.next
        else:
            curr = self.head
            while curr is not None:
                if curr.data == item:
                    if curr.next is not None:
                        curr.next.prev = curr.prev
                    curr.prev.next = curr.next

    def is_empty(self) -> bool:
        return self.head is None


class Test(unittest.TestCase):
    def test_singly_linked_list(self):
        singly_linked_list = SinglyLinkedList()
        for i in range(1, 10):
            singly_linked_list.insert(i)

        self.assertEqual(str(singly_linked_list), "9->8->7->6->5->4->3->2->1->None")
        singly_linked_list.delete(9)
        self.assertEqual(str(singly_linked_list), "8->7->6->5->4->3->2->1->None")
        singly_linked_list.delete(1)
        self.assertEqual(str(singly_linked_list), "8->7->6->5->4->3->2->None")
        singly_linked_list.delete(5)
        self.assertEqual(str(singly_linked_list), "8->7->6->4->3->2->None")

    def test_doubly_linked_list(self):
        doubly_linked_list = DoublyLinkedList()

        for i in range(3):
            doubly_linked_list.insert(i)
            self.assertEqual(doubly_linked_list.search(i).data, i)

        doubly_linked_list.delete(2)
        doubly_linked_list.delete(1)
        doubly_linked_list.delete(0)
        self.assertEqual(doubly_linked_list.is_empty(), True)


if __name__ == "__main__":
    unittest.main()
