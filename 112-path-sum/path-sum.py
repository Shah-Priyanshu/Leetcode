# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        # Base case: if the root is None, then return False since we can't have a path in an empty tree
        if not root:
            return False
        
        # Subtract the current node's value from the target sum
        targetSum -= root.val
        
        # If the current node is a leaf (no children) and the targetSum is 0, we've found a path
        if not root.left and not root.right and targetSum == 0:
            return True
        
        # Recursively check the left and right subtrees
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
