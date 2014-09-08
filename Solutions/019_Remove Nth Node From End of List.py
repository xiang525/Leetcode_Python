# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @return a ListNode

    def removeNthFromEnd(self, head, n):
        fast, slow, prev = head, head, None
        while n > 0:
            fast, n = fast.next, n - 1
        while fast != None:
            fast, slow, prev = fast.next, slow.next, slow
        if prev == None:
            return head.next
        prev.next = prev.next.next
        return head
