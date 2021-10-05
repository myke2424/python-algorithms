from typing import Any


class Node:
    """ Used for singly-linked-list practice problems """

    def __init__(self, item: Any):
        self.item: Any = item
        self.next: Node = None
