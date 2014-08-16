# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a boolean

    def hasCycle(self, head):
        fastP = head
        slowP = head
        while fastP != None and fastP.next != None:
            fastP = fastP.next.next
            slowP = slowP.next
            if fastP == slowP:
                return True
        return False
