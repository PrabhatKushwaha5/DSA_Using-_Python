
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def insertAtEnd(self, head, x):
        #code here
        new_node = Node(x)
        
        if not head:
            return new_node
            
        curr = head
        while curr.next is not None:
            curr = curr.next
            
        curr.next = new_node
        return head
                
        
def printLL(head):
    curr = head
    while curr:
        print(curr.data,end=" -> " if curr.next else " ")
        curr = curr.next
    print()


arr = list(map(int, input().split()))

obj = Solution()
head = None

for val in arr:
    head = obj.insertAtEnd(head,val)

x = int(input())
head = obj.insertAtEnd(head,x)

print("Updated LL")
printLL(head)
