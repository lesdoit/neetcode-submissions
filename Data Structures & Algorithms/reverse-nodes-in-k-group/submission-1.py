# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1: return head

        def rev_ll(head, k):
            prev, cur = None, head
            cnt = k
            while cur and cnt > 0: 
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
                cnt -= 1
            if cnt == 0: return (prev, cur)
            else: 
                h, nxt = rev_ll(prev, k - cnt)
                return (h, None)
        
        def print_dbg(head):
            print("Printing ll")
            cur = head 
            while cur:
                print(f"val: {cur.val}")
                cur = cur.next

        prev_start_before_inv = head
        cur_start_after_inv, end = rev_ll(prev_start_before_inv, k)
        head = cur_start_after_inv
        while end:
            cur_start_before_inv = end 
            cur_start_after_inv, end = rev_ll(end, k)
            prev_start_before_inv.next = cur_start_after_inv 
            prev_start_before_inv = cur_start_before_inv
            
        
        return head