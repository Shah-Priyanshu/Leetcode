# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        
        # Initialize two pointers, slow and fast
        slow = head
        fast = head
        
        # Loop to find if there's a cycle
        while fast is not None and fast.next is not None:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps
            
            # Check if slow and fast meet
            if slow == fast:
                # Move slow pointer back to head
                slow = head
                # Move slow and fast one step at a time
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                # When they meet again, it's the start of the cycle
                return slow
        
        # If we reach here, there is no cycle
        return None
