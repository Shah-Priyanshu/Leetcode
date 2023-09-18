# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """       
        h = head
        while h and h.next:
            if h.val == h.next.val:
                h.next = h.next.next
            else:
                h=h.next
        return head 