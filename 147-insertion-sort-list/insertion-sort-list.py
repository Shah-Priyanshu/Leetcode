# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sorted_head = ListNode(0)
        current = head
        
        while current:
            prev = sorted_head  
            next_node = current.next 
            while prev.next and prev.next.val < current.val:
                prev = prev.next
            
            current.next = prev.next
            prev.next = current
            
            current = next_node
        
        return sorted_head.next