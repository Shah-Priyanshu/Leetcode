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
        head_less, head_grater = ListNode(), ListNode()
        left_end, right_end = head_less, head_grater
        while head:
            if head.val < x:
                left_end.next = head
                left_end = left_end.next
            else:
                right_end.next = head
                right_end = right_end.next
            head = head.next
        left_end.next = head_grater.next
        right_end.next = None
        return head_less.next