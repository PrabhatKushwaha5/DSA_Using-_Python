class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    
    def removeNthFromEnd(self, A, B):
        
        length = 0
        temp = A
        while temp:
            length += 1
            temp = temp.next

        
        if B >= length:
            return A.next

        
        pos = length - B
        temp = A
        for _ in range(pos - 1):
            temp = temp.next

        
        if temp.next:
            temp.next = temp.next.next

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
    # Example 1
    values = [1, 2, 3, 4, 5]
    B = 2
    head = createLinkedList(values)
    print("Original Linked List:")
    printLinkedList(head)

    solution = Solution()
    new_head = solution.removeNthFromEnd(head, B)

    print(f"After removing {B}th node from end:")
    printLinkedList(new_head)

    # Example 2
    values = [1]
    B = 1
    head = createLinkedList(values)
    print("\nOriginal Linked List:")
    printLinkedList(head)

    new_head = solution.removeNthFromEnd(head, B)
    print(f"After removing {B}th node from end:")
    printLinkedList(new_head)
