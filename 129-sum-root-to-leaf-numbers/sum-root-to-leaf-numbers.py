# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, currentSum):
            if not node:
                return 0
            currentSum = currentSum * 10 + node.val
            # If it's a leaf node, return the current sum
            if not node.left and not node.right:
                return currentSum
            # Continue the depth-first search on child nodes
            return dfs(node.left, currentSum) + dfs(node.right, currentSum)
        
        return dfs(root, 0)
