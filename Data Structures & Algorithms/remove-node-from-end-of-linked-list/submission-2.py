# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # approach 2 - use explicit stack to revese, remove, reverse again
        
        dummy = ListNode(-1, head)
        head = dummy
        
        dq = deque()
        cur = head 
        while cur:
            dq.append(cur)
            cur = cur.next
        
        for _ in range(n):
            dq.pop()
        
        prev = dq[-1]
        
        to_remove = prev.next
        print(f"to remove val: {to_remove.val}")
        
        prev.next = prev.next.next
        to_remove.next = None
        # print(f"prev.nxt val: {prev.next.val}")
        
        # clean up stack 
        dq.clear()
        head = dummy.next 
        dummy.next = None 
        
        return head

