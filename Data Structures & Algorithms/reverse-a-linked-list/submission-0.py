# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        add = []
        while head:
            add.append(head)
            head = head.next
        
        for i in range(len(add)-1,-1,-1):
            if i-1 < len(add) and i - 1 > -1:
                add[i].next = add[i-1]

        add[0].next = None
        return add[-1]