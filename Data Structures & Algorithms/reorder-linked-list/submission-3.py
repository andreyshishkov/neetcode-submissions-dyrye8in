# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the middle of linked list
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        middle = slow.next
        slow.next = None

        # reverse second half
        prev = None
        while middle:
            tmp = middle.next
            middle.next = prev
            prev = middle
            middle = tmp
        rev_half = prev

        # merge two lists
        curr = head
        while rev_half and curr:
            tmp_curr = curr.next
            tmp_rev = rev_half.next

            curr.next = rev_half
            rev_half.next = tmp_curr

            curr = tmp_curr
            rev_half = tmp_rev

        

        
        
        
        