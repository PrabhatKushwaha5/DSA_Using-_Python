class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def searchKey(self, head, key):
        curr = head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

def printList(head):
    curr = head
    while curr:
        print(curr.data, end=" -> " if curr.next else "")
        curr = curr.next
    print()

if __name__ == "__main__":
    n1 = Node(10)
    n2 = Node(20)
    n3 = Node(30)
    n4 = Node(40)
    n1.next = n2
    n2.next = n3
    n3.next = n4

    sol = Solution()
    printList(n1)
    print(sol.searchKey(n1, 20))  # True
    print(sol.searchKey(n1, 50))  # False
