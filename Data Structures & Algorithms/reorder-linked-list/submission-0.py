# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def rec_del(self, head):
        if not head: return
        if not head.next: 
            head = None
            return
        self.rec_del(head.next)
        head = None 
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1st approach - use a stack
        # 2nd approach - reverse second half of the ll and then merge with first half

        dq = deque() 
        n = 0 
        cur = head
        while cur:
            dq.append(cur)
            cur = cur.next
            n += 1
        
        print(f"n: {n}")
        for elem in dq:
            print(f"elem: {elem}, {elem.val}")

        # if n is even, then join n/2 top elements from stack 

        # if n is odd, then join floor(n/2) top elements from stack 

        # in both cases, deallocate the rest of the linkedlist as an exercise. 
        # Do not just rely on the GC 
        
        # print(f"int n/2: {int(n/2)}")
        # cur = head
        # print(f"head: {cur}")

        # print(f"dq.pop(): {dq.pop()}")
        # tail = dq.pop()
        # print(f"tail: {tail}")
        # tail.next = cur.next
        cur = head
        for i in range(int(n/2)):
            tail = dq.pop()
            tail.next = cur.next
            cur.next = tail 
            cur = tail.next

        cur.next = None
        
        # self.rec_del(cur)
        # cur = None
        


