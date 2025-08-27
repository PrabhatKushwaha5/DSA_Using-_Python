class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        if fast is None:
            return head.next
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2
s = Solution()
new_head = s.removeNthFromEnd(head, n)

while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next
