# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and not list2:
            return list1
        
        if not list1 and list2:
            return list2

        # always make list1 consume list2 
        l1head = list1
        l1prev = None

        while list1 and list2:
            if list1.val > list2.val:
                tmp = list2
                list2 = list2.next
                if l1prev:
                    l1prev.next = tmp
                    l1prev = tmp
                else:
                    l1prev = tmp 
                    l1head = l1prev
                tmp.next = list1
            else:
                l1prev = list1
                list1 = list1.next

        if list2:
            # add remaining elements of list2 to list1
            l1prev.next = list2
        
        return l1head
