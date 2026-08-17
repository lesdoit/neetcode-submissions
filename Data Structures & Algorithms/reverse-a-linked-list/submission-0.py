# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        nhead = None
        
        def recurse(node):
            if not node.next:
                nonlocal nhead
                nhead = node 
                return 
            recurse(node.next)
            node.next.next = node
            node.next = None
        
        recurse(head)
        
        return nhead

        