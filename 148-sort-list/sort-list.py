# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        # Base case: if the list is empty or has a single element, it's already sorted
        if not head or not head.next:
            return head
        
        # Step 1: Split the list into halves
        left_end, slow, fast = None, head, head
        while fast and fast.next:
            left_end, slow, fast = slow, slow.next, fast.next.next
        left_end.next = None  # Cut the list into two halves
        
        # Step 2: Sort each half recursively
        left = self.sortList(head)
        right = self.sortList(slow)
        
        # Step 3: Merge the sorted halves
        return self.merge(left, right)
    
    def merge(self, left, right):
        # Helper function to merge two sorted lists
        dummy = ListNode(0)
        tail = dummy
        while left and right:
            if left.val < right.val:
                tail.next, left = left, left.next
            else:
                tail.next, right = right, right.next
            tail = tail.next
        tail.next = left or right
        
        return dummy.next