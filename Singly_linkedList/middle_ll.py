class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LL:
    def __init__(self):
        self.head = None

    
    def Append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    
    def middle(self):
        slow = fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    
    def Traversal(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> " if curr.next else "\n")
            curr = curr.next



ll = LL()
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    ll.Append(val)

print("\nLinked list:")
ll.Traversal()

middle_node = ll.middle()
if middle_node:
    print("\nMiddle node value:", middle_node.data)
else:
    print("\nThe list is empty.")
