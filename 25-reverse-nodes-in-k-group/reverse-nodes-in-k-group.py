# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = jump = ListNode()
        dummy.next = left = right = head

        while True:
            # First count number of available nodes (up to k)
            num_nodes = 0
            while right and num_nodes < k:
                right = right.next
                num_nodes += 1
            # We are at a set of left-out nodes (last block of nodes)
            if num_nodes != k:
                return dummy.next
            else:
                # Reverse this set of k nodes
                prev, curr = right, left
                for iteration in range(k):
                    curr.next, curr, prev = prev, curr.next, curr
                jump.next, jump, left = prev, left, right