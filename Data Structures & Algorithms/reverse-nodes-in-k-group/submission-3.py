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
        
        dummy = ListNode(-1, head)
        prev_group_tail = dummy

        cur_group_head_before_inv = prev_group_tail.next
        while cur_group_head_before_inv:
            cur_group_head_after_inv, next_group_head = rev_ll(cur_group_head_before_inv, k)
            prev_group_tail.next = cur_group_head_after_inv
            if next_group_head: 
                cur_group_head_before_inv.next = next_group_head
            prev_group_tail = cur_group_head_before_inv
            cur_group_head_before_inv = next_group_head
            # cur_group_head_after_inv, next_group_head = rev_ll(cur_group_head_before_inv, k)
        

        
        return dummy.next