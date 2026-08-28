# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        add = []
        while head:
            add.append(head)
            head = head.next
        
        target = len(add) - n
        if len(add) == 1: return None
        if not target + 1 > len(add) - 1 and not target - 1 < 0: 
            add[target - 1].next = add[target + 1]
        elif target - 1 < 0 and not target + 1 > len(add) - 1:
            return add[target + 1]
        else:
            add[target - 1].next = None

        return add[0]