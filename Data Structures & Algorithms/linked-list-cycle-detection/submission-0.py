# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []
        if not head or  not head.next: return False
        current = head
        while current.next:
            if current.next in visited: return True
            visited.append(current)
            current = current.next  

        return False