class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getLength(head):
    count = 0
    curr = head
    while curr:
        count += 1
        curr = curr.next
    return count

def printList(head):
    curr = head
    while curr:
        print(curr.data, end=" -> " if curr.next else "")
        curr = curr.next
    print()

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5

    printList(n1)
    print(getLength(n1))
