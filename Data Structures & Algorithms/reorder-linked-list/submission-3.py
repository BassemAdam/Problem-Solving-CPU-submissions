# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        addresses = []
        current = head
        while current:
            addresses.append(current)
            current = current.next
        n = len(addresses) - 1
        if n == 0 or n == 1  : return 
        right = n
        left = 0
        while left < right:
            addresses[left].next = addresses[right]
            print(f"p-A left : {left} right : {right}")
            left +=1
            if left < right:
                addresses[right].next = addresses[left]
                print(f"p-B left : {left} right : {right}")
            right -=1
        
        if n % 2 == 1:
            addresses[n//2 + 1].next = None
        else:
            addresses[n//2].next = None
    

