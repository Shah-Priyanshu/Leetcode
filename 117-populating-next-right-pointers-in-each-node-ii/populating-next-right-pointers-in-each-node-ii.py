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
        
        leftmost = root
        
        while leftmost:
            # Start the current level
            cur = leftmost
            
            # Dummy node to kickstart the next level
            dummy = Node(0)
            tail = dummy
            
            # Reset leftmost to None to find the new leftmost for the next level
            leftmost = None
            
            while cur:
                # Connect the left child if it exists
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                    if not leftmost:
                        leftmost = cur.left
                        
                # Connect the right child if it exists
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                    if not leftmost:
                        leftmost = cur.right
                        
                # Move to the next node in the current level
                cur = cur.next
            
        return root
