# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next
        
        start_prev = prev
        start = prev.next

        prev2 = None
        cur = start
        for _ in range(right - left + 1):
            next_node = cur.next
            cur.next = prev2
            prev2 = cur
            cur = next_node

        start_prev.next = prev2
        start.next = cur
        return dummy.next