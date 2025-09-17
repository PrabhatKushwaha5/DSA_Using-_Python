# Definition for singly-linked list node
class node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def deleteK(self, head, k):
        # Edge cases
        if not head or k <= 0:
            return head
        if k == 1:   # remove every node
            return None

        dummy = node(0)
        dummy.next = head
        prev, curr = dummy, head
        count = 1

        while curr:
            if count % k == 0:
                # skip this node
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
            count += 1

        return dummy.next


# ---------------------------
# Helper functions for testing
# ---------------------------

def build_linked_list(values):
    """Builds linked list from list of values and returns head"""
    if not values:
        return None
    head = node(values[0])
    curr = head
    for val in values[1:]:
        curr.next = node(val)
        curr = curr.next
    return head

def print_linked_list(head):
    """Prints the linked list"""
    res = []
    curr = head
    while curr:
        res.append(str(curr.data))
        curr = curr.next
    print(" -> ".join(res))


# ---------------------------
# Example usage
# ---------------------------

if __name__ == "__main__":
    # Example: Linked list = 1->2->3->4->5->6->7->8, k=2
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 2
    head = build_linked_list(arr)

    print("Original list:")
    print_linked_list(head)

    sol = Solution()
    new_head = sol.deleteK(head, k)

    print(f"\nList after deleting every {k}-th node:")
    print_linked_list(new_head)
