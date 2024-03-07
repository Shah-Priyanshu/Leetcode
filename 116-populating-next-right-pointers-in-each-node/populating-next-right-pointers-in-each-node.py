class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        # Start with the root node
        leftmost = root
        while leftmost.left:
            # Iterate through the nodes in the current level
            head = leftmost
            while head:
                # Connect the left child to the right child
                head.left.next = head.right
                # Connect the right child to the next node's left child, if exists
                if head.next:
                    head.right.next = head.next.left
                
                # Move to the next node in the current level
                head = head.next
            
            # Move to the leftmost node of the next level
            leftmost = leftmost.left
        
        return root
