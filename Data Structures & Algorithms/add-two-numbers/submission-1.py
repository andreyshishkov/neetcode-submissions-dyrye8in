# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = 0
        head = ListNode()
        curr = head
        res = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            value = l1_val + l2_val + res
            digit = value % 10
            res = value // 10

            node = ListNode(digit)
            curr.next = node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next

        if res:
            curr.next = ListNode(res)
        return head.next

        