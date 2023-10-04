# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy
        
        while head and head.next:
            # Nodes to be swapped
            first_node = head
            second_node = head.next
            
            # Swapping logic
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            # Reinitializing the head and prev_node for next pair
            prev_node = first_node
            head = first_node.next
            
        return dummy.next