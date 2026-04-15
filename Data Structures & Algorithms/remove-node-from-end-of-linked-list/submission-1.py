# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        k = 0
        first = head
        second = dummy
        while k < n and first:
            first = first.next
            k += 1
        
        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next
