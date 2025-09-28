class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def constructDLL(self, arr):
        if not arr:
            return None
        head = Node(arr[0])
        curr = head
        for i in range(1, len(arr)):
            new_node = Node(arr[i])
            curr.next = new_node
            new_node.prev = curr
            curr = new_node
        return head

def printDLL(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        last = curr
        curr = curr.next
    print()


arr = [1, 2, 3, 4, 5]
obj = Solution()
head = obj.constructDLL(arr)
printDLL(head)
