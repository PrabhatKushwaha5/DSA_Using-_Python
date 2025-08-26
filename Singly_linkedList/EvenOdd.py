class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def oddEvenList(head):
    if head is None or head.next is None:
        return head
    odd = head
    even = head.next
    even_head = even
    while even is not None and even.next is not None:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next
    odd.next = even_head
    return head

def printList(head):
    curr = head
    while curr:
        print(curr.value, end=" ")
        curr = curr.next
    print()

def createList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        head = createList(arr)
        new_head = oddEvenList(head)
        printList(new_head)
