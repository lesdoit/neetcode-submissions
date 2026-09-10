# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
from itertools import count

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        tie_breaker = count()
        heap = []
        for item in lists:
            if item:
                heap.append((item.val, next(tie_breaker), item))
        heapq.heapify(heap)

        head = ListNode()
        cur = head
        while heap:
            top = heapq.heappop(heap)
            
            if top[2].next:
                heapq.heappush(heap, (top[2].next.val, next(tie_breaker), top[2].next))

            cur.next = top[2]
            cur = cur.next
        
        return head.next