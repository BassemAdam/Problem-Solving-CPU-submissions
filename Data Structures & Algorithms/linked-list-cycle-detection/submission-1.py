# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # solution 1
        # visited = []
        # if not head or  not head.next: return False
        # current = head
        # while current.next:
        #     if current.next in visited: return True
        #     visited.append(current)
        #     current = current.next  

        # return False

        # solution 2
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True
        return False