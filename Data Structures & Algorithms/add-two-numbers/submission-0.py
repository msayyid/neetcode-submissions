# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         cur1 = l1
#         digit1 = []
#         while cur1:
#             digit1.append(str(cur1.val))
#             cur1 = cur1.next

#         cur2 = l2
#         digit2 = []
#         while cur2:
#             digit2.append(str(cur2.val))
#             cur2 = cur2.next

#         digit1 = int("".join(digit1))
#         digit2 = int("".join(digit2))

#         # print(digit1 + digit2)
#         final = digit1 + digit2
#         final = reversed(str(final))
#         dummy = ListNode(0)
#         cur = dummy
#         for num in final:
#             cur.next = ListNode(num)
#             cur = cur.next

#         # print()
#         return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        cur1 = l1
        dig1 = []
        while cur1:
            dig1.append(str(cur1.val))
            cur1 = cur1.next

        cur2 = l2
        dig2 = []
        while cur2:
            dig2.append(str(cur2.val))
            cur2 = cur2.next

        dig1 = int("".join(reversed(dig1)))
        dig2 = int("".join(reversed(dig2)))
        # print(dig1 + dig2)

        final = dig1 + dig2
        final = str(final)
        # print(type(final))
        dummy = ListNode(0)
        cur = dummy
        for num in reversed(final):
            cur.next = ListNode(int(num))
            cur = cur.next
        # print(dummy.next)
        return dummy.next