# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1 = l1
        cur2 = l2

        dummy = ListNode(0)
        start = dummy

        # stores the carry from the previous additions
        carry = 0

        # continue while either list has nodes or
        # a carry remains
        while cur1 or cur2 or carry:

            # get the current digits
            # use 0 if a list has no remaining nodes
            digit1 = 0 if not cur1 else cur1.val
            digit2 = 0 if not cur2 else cur2.val
            
            total = digit1 + digit2 + carry

            node = total % 10
            carry = total // 10

            start.next = ListNode(node)
            start = start.next
            if cur2:
                cur2 = cur2.next
            if cur1:
                cur1 = cur1.next
        # print(dummy.next)
        
        return dummy.next


            