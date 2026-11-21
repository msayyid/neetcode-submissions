# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        digit1 = []
        while cur1:
            digit1.append(str(cur1.val))
            cur1 = cur1.next

        cur2 = l2
        digit2 = []
        while cur2:
            digit2.append(str(cur2.val))
            cur2 = cur2.next

        digit1 = int("".join(reversed(digit1)))
        digit2 = int("".join(reversed(digit2)))

        # print(digit1 + digit2)
        final = digit1 + digit2
        final = str(final)
        dummy = ListNode(0)
        cur = dummy
        for num in reversed(final):
            cur.next = ListNode(num)
            cur = cur.next

        # print()
        return dummy.next