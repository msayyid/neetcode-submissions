# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head

        # this way first half will more or equal number of nodes as second half
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None

        prev = None
        while second_half:
            next_node = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = next_node
        cur = head
        while prev:
            next_node = cur.next
            prev_next = prev.next

            cur.next = prev
            prev.next = next_node

            cur = next_node
            prev = prev_next
        

        