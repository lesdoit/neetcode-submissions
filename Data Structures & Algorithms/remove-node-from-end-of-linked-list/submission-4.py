# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # approach 1 - reverse, remove, reverse 

        def reverse_ll(head): 
            prev, cur = None, head
            while cur: 
                tmp = cur.next 
                cur.next = prev
                prev = cur 
                cur = tmp
            return prev
         
        head = reverse_ll(head)

        dummy = ListNode(0, head)
        head = dummy 
        cur = head 
        while n > 1 and cur: 
            cur = cur.next
            n -= 1

        removal_node = cur.next
        cur.next = removal_node.next
        removal_node.next = None
        
        head = dummy.next

        head = reverse_ll(head)
        return head

