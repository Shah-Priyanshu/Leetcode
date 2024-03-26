class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
            
        # Step 1: Clone each node and insert it right next to the original node
        current = head
        while current:
            cloned = Node(current.val, current.next, None)
            current.next = cloned
            current = cloned.next
            
        # Step 2: Copy the random pointers
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
            
        # Step 3: Separate the original list from the cloned list
        current = head
        clone_head = head.next
        while current:
            cloned = current.next
            current.next = cloned.next
            current = current.next
            if cloned.next:
                cloned.next = cloned.next.next
            
        return clone_head
