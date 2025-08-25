class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Solution:
    def reverseList(self, head):
        prev = None
        temp = head

        while temp is not None:
            front = temp.next    
            temp.next = prev     
            prev = temp         
            temp = front         

        return prev 
    

def createLL(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

def printLL(head):
    curr = head
    while curr:
        print(curr.data,end="->")
        curr = curr.next
    print("None")



if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    head = createLL(arr)
    print("Original List:")
    printLL(head)

    sol = Solution()
    reversed_head = sol.reverseList(head)

    print("Reversed List:")
    printLL(reversed_head)
        