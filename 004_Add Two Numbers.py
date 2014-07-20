class Solution:
    # @return a ListNode

    def addTwoNumbers(self, l1, l2):
        carry = 0
        head = ListNode(0)
        curr = head
        while l1 and l2:
            Sum = l1.val + l2.val + carry
            carry = Sum / 10
            curr.next = ListNode(Sum % 10)
            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        while l1:
            Sum = l1.val + carry
            carry = Sum / 10
            curr.next = ListNode(Sum % 10)
            l1 = l1.next
            curr = curr.next
        while l2:
            Sum = l2.val + carry
            carry = Sum / 10
            curr.next = ListNode(Sum % 10)
            l2 = l2.next
            curr = curr.next
        if carry > 0:
            curr.next = ListNode(carry)
        return head.next
