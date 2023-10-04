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
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head

        # Initialize two pointers, first and second
        first = dummy
        second = dummy

        # Move the first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # Move both pointers until the first pointer reaches the end
        while first is not None:
            first = first.next
            second = second.next

        # Remove the nth node by updating the next pointer of the previous node
        second.next = second.next.next

        return dummy.next