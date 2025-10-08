class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None

class Solution:
    def reverse(self, head):
        if not head:
            return None
        curr = head
        temp = None
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        if temp:
            head = temp.prev
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
    print_doubly_linked_list(head)
    sol = Solution()
    head = sol.reverse(head)
    print_doubly_linked_list(head)
