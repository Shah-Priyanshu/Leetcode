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
        # Helper function to reverse a sublist of k nodes
        def reverse(head, k):
            prev = None
            curr = head
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev

        # Count the total number of nodes in the linked list
        def countNodes(head):
            count = 0
            while head:
                count += 1
                head = head.next
            return count

        # Calculate the number of groups
        num_groups = countNodes(head) // k

        dummy = ListNode(0)
        dummy.next = head
        prev_group_tail = dummy
        curr_group_head = head

        for _ in range(num_groups):
            next_group_head = curr_group_head
            for _ in range(k - 1):
                if next_group_head:
                    next_group_head = next_group_head.next

            if not next_group_head:
                break

            next_group_head_next = next_group_head.next
            next_group_head.next = None

            # Reverse the current group of k nodes
            new_group_head = reverse(curr_group_head, k)

            # Connect the reversed group to the previous group
            prev_group_tail.next = new_group_head

            # Move pointers for the next iteration
            curr_group_head.next = next_group_head_next
            prev_group_tail = curr_group_head
            curr_group_head = next_group_head_next

        return dummy.next