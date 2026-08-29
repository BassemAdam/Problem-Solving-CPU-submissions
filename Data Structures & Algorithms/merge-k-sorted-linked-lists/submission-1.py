# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        answer = ListNode()
        traverser = answer
        for i,ptr in enumerate(lists):
            if ptr:
                heapq.heappush(heap,(ptr.val,i,ptr))
        while heap:
            val,i,ptr = heapq.heappop(heap)
            traverser.next = ptr
            traverser = traverser.next
            if ptr.next:
                heapq.heappush(heap,(ptr.next.val,i, ptr.next))
        return answer.next
