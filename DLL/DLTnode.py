class Node:
    def __init__(self, d):
        self.data = d
        self.prev = None
        self.next = None


class Solution:
    def delPos(self, head, x):
        if not head:
            return None

        if x == 1:
            head = head.next
            if head:
                head.prev = None
            return head

        curr = head
        count = 1
        while curr and count < x:
            curr = curr.next
            count += 1

        if not curr:
            return head

        if curr.prev:
            curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev

        return head


def build_doubly_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for val in values[1:]:
        new_node = Node(val)
        curr.next = new_node
        new_node.prev = curr
        curr = new_node
    return head


def print_doubly_linked_list(head):
    curr = head
    while curr:
        print(curr.data, end=" <-> " if curr.next else "\n")
        curr = curr.next


if __name__ == "__main__":
    head = build_doubly_linked_list([1, 2, 3, 4, 5])
    print("Original List:")
    print_doubly_linked_list(head)

    sol = Solution()
    head = sol.delPos(head, 3)
    print("\nAfter deleting node at position 3:")
    print_doubly_linked_list(head)
