# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast, slow = head, head
        while n > 0: #advance fast n pointers
            fast = fast.next
            n -= 1
        if not fast:
            return head.next
        while fast and fast.next is not None:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return head