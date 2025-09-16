class Node:
    def __init__(self, data):
            self.data = data
            self.next = None

class Solution:    
    def pairWiseSwap(self, head):
        # code here
        prev = head
        curr = prev.next
        while prev and prev.next:
            prev = curr
            curr = prev
            prev = prev.next.next
            curr = curr.next.next
        return head