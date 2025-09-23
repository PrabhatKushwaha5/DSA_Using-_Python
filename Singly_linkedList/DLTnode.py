class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
    
    n1 = Node(4)
    n2 = Node(5)
    n3 = Node(1)
    n4 = Node(9)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    sol = Solution()
   
    sol.deleteNode(n2)

    printList(n1)  
