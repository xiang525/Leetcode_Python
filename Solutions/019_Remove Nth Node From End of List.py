# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @return a ListNode

    def removeNthFromEnd(self, head, n):
        fast = head
        slow = head
        prev = None
        while n > 0:
            fast = fast.next
            n -= 1 
        while fast != None:
            fast = fast.next
            slow = slow.next
            prev = slow
        if prev == None:
            return head.next
        prev.next = prev.next.next
        return head
