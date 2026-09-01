# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # approach 3 - use implicit stack to reverse, remove
        # Dummy node handles the edge case where the original head is removed
        dummy = ListNode(0, head)
        
        def remove(node: Optional[ListNode]) -> int:
            if not node:
                return 0
            
            # Recurse to the end (Implicit Stack Push)
            idx_from_end = remove(node.next) + 1
            
            # Unwinding Phase (Implicit Stack Pop):
            # If the current node is immediately before the target (n + 1 from end)
            if idx_from_end == n + 1:
                to_remove = node.next
                node.next = to_remove.next
                to_remove.next = None  # Clean up reference
                
            return idx_from_end

        remove(dummy)
        return dummy.next

