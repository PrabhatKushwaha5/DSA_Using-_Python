
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next           
            fast = fast.next.next      

            if slow == fast:
                return True            

        return False                   



def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def createCycle(head, pos):
    if pos == -1 or not head:
        return head
    cycleNode = None
    curr = head
    idx = 0
    last = None
    while curr:
        if idx == pos:
            cycleNode = curr
        last = curr
        curr = curr.next
        idx += 1
    if last and cycleNode:
        last.next = cycleNode
    return head


if __name__ == "__main__":
    arr = [3, 2, 0, -4]

    
    head1 = createLinkedList(arr)
    head1 = createCycle(head1, 1)

    sol = Solution()
    print("Has Cycle (Case 1):", sol.hasCycle(head1)) 

   
    head2 = createLinkedList(arr)
    print("Has Cycle (Case 2):", sol.hasCycle(head2))  
