# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, A):
        if not A or not A.next:
            return A

        current = A
        while current and current.next:
            if current.val == current.next.val:
                
                current.next = current.next.next
            else:
                current = current.next

        return A



# Helper functions for testing

def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next




if __name__ == "__main__":
    # Example input: 1 -> 1 -> 2 -> 3 -> 3
    values = [1, 1, 2, 3, 3]
    head = createLinkedList(values)

    print("Original Linked List:")
    printLinkedList(head)

    # Remove duplicates
    solution = Solution()
    new_head = solution.deleteDuplicates(head)

    print("After Removing Duplicates:")
    printLinkedList(new_head)
