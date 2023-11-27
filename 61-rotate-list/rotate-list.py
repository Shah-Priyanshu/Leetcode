# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next or k == 0:
            return head

        # Find the length of the linked list and the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Calculate the effective rotation
        k = k % length
        if k == 0:
            return head

        # Fast forward to the new tail node
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # Update pointers to rotate the list
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head
