class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Handle the edge case of an empty list or a single node
        if not head or not head.next:
            return head

        # Create a dummy node to simplify the deletion process
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            if current.next.val == current.next.next.val:
                # Skip all duplicates at once
                val_to_remove = current.next.val
                while current.next and current.next.val == val_to_remove:
                    current.next = current.next.next
            else:
                current = current.next

        return dummy.next
