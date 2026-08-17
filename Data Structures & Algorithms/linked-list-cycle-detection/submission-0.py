# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head 
        ans = False
        
        while fast.next:
            fast = fast.next.next
            if fast is None:
                break
            elif fast == slow:
                ans = True
                break
            slow = slow.next
        return ans