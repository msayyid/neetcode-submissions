# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1 = list1
        cur2 = list2
        dummy = ListNode(0)
        the_one = dummy
        while cur1 and cur2:
            if cur1.val < cur2.val:
                the_one.next = cur1
                cur1 = cur1.next
                # the_one = the_one.next
            else:
                the_one.next = cur2
                cur2 = cur2.next
                # the_one = the_one.next
            the_one = the_one.next
            
        if cur1:
            the_one.next = cur1
        else:
            the_one.next = cur2
        return dummy.next