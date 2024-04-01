# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack, output = [root], []
        
        while stack:
            node = stack.pop()
            if node:
                output.append(node.val)
                # Right child is pushed first so that left is processed first
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        
        return output
