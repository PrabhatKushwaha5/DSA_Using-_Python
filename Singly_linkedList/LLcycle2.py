
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        
        slow, fast = head, head

        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  
                break
        else:
            
            return None

        
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  



def printCycleStart(head):
    sol = Solution()
    start_node = sol.detectCycle(head)
    if start_node:
        print("Cycle starts at node with value:", start_node.val)
    else:
        print("No cycle detected.")


head1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

head1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2  

printCycleStart(head1)  

# Example 2: No cycle
head2 = ListNode(1)
head2.next = ListNode(2)

printCycleStart(head2)  
