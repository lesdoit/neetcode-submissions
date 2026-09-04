# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def removeLastIfZero(head):
            if not head: 
                return 0
            
            idx_from_last = removeLastIfZero(head.next) + 1
            if idx_from_last == 2 and head.next.val == 0:
                head.next = head.next.next
            return idx_from_last
        
        c1, c2 = l1, l2
        carry = 0
        c3 = ListNode()
        ans = c3 
        while c1 and c2: 
            c3.val = (c1.val + c2.val + carry)%10
            carry = (c1.val + c2.val + carry)//10
            c3.next = ListNode()
            c3 = c3.next
            c1 = c1.next 
            c2 = c2.next
        
        # remaining c1
        while c1: 
            c3.val = (c1.val + carry)%10
            carry = (c1.val + carry)//10
            c3.next = ListNode()
            c3 = c3.next
            c1 = c1.next
        
        # remaining c2
        while c2: 
            c3.val = (c2.val + carry)%10
            carry = (c2.val + carry)//10
            c3.next = ListNode()
            c3 = c3.next
            c2 = c2.next
        
        # leftover carry 
        c3.val = carry 
        
        removeLastIfZero(ans)
        
        return ans
        