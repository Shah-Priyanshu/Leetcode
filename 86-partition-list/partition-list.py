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
        
        from collections import deque

        lt = deque([])    
        e_gt = deque([])
        curr = head

        while curr:
            if curr.val < x: lt.append(curr.val)
            else: e_gt.append(curr.val)
            curr = curr.next
        
        curr = head

        while lt:
            curr.val = lt[0]
            lt.popleft()
            curr = curr.next
        
        while e_gt:
            curr.val = e_gt[0]
            e_gt.popleft()
            curr = curr.next

        return head