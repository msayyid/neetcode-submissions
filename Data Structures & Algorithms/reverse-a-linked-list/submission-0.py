# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if not head:
            return head
        cur = head
        prev = None
        stack = []
        count = 0
        count2 = 0
        while cur:
            stack.append(cur)
            count += 1
            cur = cur.next
            count2 += 1
        
        while stack:
            if count == count2:
                head = stack.pop()
                cur = head
                count2 -= 1
            else:
                cur.next = stack.pop()
                cur = cur.next
        cur.next = None
        return head