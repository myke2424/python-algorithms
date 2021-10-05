from .linked_list import Node


# Time: O(N) | Space: O(N)
def remove_dups(head: Node) -> Node:
    """ Removed duplicates from an unsorted linked list """

    # In order to remove duplicates, we want to track duplicates via a hash table or set.
    node_set = set()
    prev = None
    node = head

    while node is not None:
        if node.data in node_set:
            prev.next = node.next
        else:
            node_set.add(node.data)
            prev = node
        node = node.next
