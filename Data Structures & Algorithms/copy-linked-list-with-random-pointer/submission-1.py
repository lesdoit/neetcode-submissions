"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # guard against degen cases
        if not head: return head

        # phase 1 - interleave the new linked list in the input 
        cur = head 
        while cur:
            y = Node(cur.val)
            y.next = cur.next
            cur.next = y
            cur = y.next
        
        # phase 2 - copy random pointer in the new secondary linked list 
        cur = head 
        while cur: 
            y = cur.next 
            if not cur.random:
                y.random = cur.random 
            else: 
                y.random = cur.random.next 
            cur = y.next 
        
        # phase 3 - destroy the interleaved secondary list 
        head2 = head.next 
        cur = head
        while cur: 
            y = cur.next 
            if not y: 
                cur.next = None
            else: 
                cur.next = y.next 
            cur = y
        
        return head2
