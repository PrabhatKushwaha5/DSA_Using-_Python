class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def lengthOfLoop(self, head):
        if not head:
            return 0
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = slow.next
                count = 1
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return 0

def build_linked_list(values, pos=-1):
    if not values:
        return None
    head = Node(values[0])
    curr = head
    nodes = [head]
    for val in values[1:]:
        new_node = Node(val)
        curr.next = new_node
        curr = new_node
        nodes.append(new_node)
    if pos != -1:
        curr.next = nodes[pos]
    return head

if __name__ == "__main__":
    head = build_linked_list([1,2,3,4,5], pos=1)
    sol = Solution()
    print(sol.lengthOfLoop(head))
