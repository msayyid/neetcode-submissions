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
        carry = 0
        while cur1 or cur2 or carry:
            digit1 = 0 if not cur1 else cur1.val
            if cur1:
                cur1 = cur1.next
            digit2 = 0 if not cur2 else cur2.val
            if cur2:
                cur2 = cur2.next
            total = digit1 + digit2 + carry

            node = total % 10
            carry = total // 10

            start.next = ListNode(node)
            start = start.next
        # print(dummy.next)
        
        return dummy.next


            