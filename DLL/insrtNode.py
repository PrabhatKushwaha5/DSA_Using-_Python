class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def insertAtPos(self, head, p, x):
        new_node = Node(x)
        if not head:
            return new_node
        curr = head
        count = 0
        while curr and count < p:
            curr = curr.next
            count += 1
        if not curr:
            return head
        next_node = curr.next
        curr.next = new_node
        new_node.prev = curr
        new_node.next = next_node
        if next_node:
            next_node.prev = new_node
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
    head = build_doubly_linked_list([1, 2, 3, 4])
    print_doubly_linked_list(head)
    sol = Solution()
    head = sol.insertAtPos(head, 1, 9)
    print_doubly_linked_list(head)
