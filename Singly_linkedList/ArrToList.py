
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def arrayToList(self, arr):
        # code here
        if not arr:
            return None
            
        head = Node(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = Node(val)
            curr = curr.next
        return head
    
def printLinkkedList(head):
    curr = head
    while curr:
        print(curr.data,end=" -> " if curr.next else "")
        curr = curr.next
    print()

arr = list(map(int,input().split()))
obj = Solution()
head = obj.arrayToList(arr)
printLinkkedList(head)