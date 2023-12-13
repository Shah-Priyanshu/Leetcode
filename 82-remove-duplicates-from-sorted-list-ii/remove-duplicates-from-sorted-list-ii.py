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
        
        dummy = ListNode(0)
        p = dummy
        p.next = head
        curr =-1

        while p.next and p.next.next:

            if p.next.val == p.next.next.val :   
                curr = p.next.val
                while p.next and p.next.val == curr:
                    p.next = p.next.next
                
            else:
                p = p.next
        
        if p.next and p.next.val == curr:
            p.next == None

        return dummy.next 
        