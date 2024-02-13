# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        # Initialize a queue with the root node and a marker for depth.
        queue = [(root, 1)]
        max_depth = 0
        
        while queue:
            # Pop the current node and its depth from the queue.
            current, depth = queue.pop(0)
            
            if current:
                # Update the max depth.
                max_depth = max(max_depth, depth)
                
                # Add the children of the current node to the queue, with their depth incremented by 1.
                if current.left:
                    queue.append((current.left, depth + 1))
                if current.right:
                    queue.append((current.right, depth + 1))
        
        return max_depth
