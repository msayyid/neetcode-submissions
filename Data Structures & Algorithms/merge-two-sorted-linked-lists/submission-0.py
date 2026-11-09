# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = list1
        cur2 = list2
        dummy = ListNode(None, None)
        new_ptr = dummy
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                new_ptr.next = cur1
                cur1 = cur1.next
            else:
                new_ptr.next = cur2
                cur2 = cur2.next
            new_ptr = new_ptr.next
        
        new_ptr.next = cur1 if cur1 else cur2
        return dummy.next