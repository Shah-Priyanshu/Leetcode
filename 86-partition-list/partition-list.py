# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # Initialize two dummy nodes for the two partitions
        before_dummy = ListNode(0)
        after_dummy = ListNode(0)

        # Pointers to the current nodes in the two partitions
        before = before_dummy
        after = after_dummy

        # Traverse the original linked list
        current = head
        while current:
            if current.val < x:
                before.next = current
                before = before.next
            else:
                after.next = current
                after = after.next

            current = current.next

        # Connect the two partitions
        before.next = after_dummy.next
        after.next = None  # Set the end of the after partition to None

        return before_dummy.next
