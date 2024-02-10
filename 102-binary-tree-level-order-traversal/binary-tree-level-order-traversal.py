class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        from collections import deque
        queue = deque([(root, 0)])  # Queue of tuples (node, level)
        levels = []  # To store the final result
        
        while queue:
            node, level = queue.popleft()
            
            # If we're entering a new level, add a sublist
            if len(levels) == level:
                levels.append([])
                
            # Append the current node's value to its level's list
            levels[level].append(node.val)
            
            # Enqueue children with their respective levels
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return levels
