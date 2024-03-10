class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Initialize the global maximum path sum with the lowest possible value
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
            
            # Recursively find the maximum path sum for the left and right children
            left_gain = max(max_gain(node.left), 0) # Ignore paths with negative sums
            right_gain = max(max_gain(node.right), 0)
            
            # Price to start a new path where `node` is the highest node
            price_newpath = node.val + left_gain + right_gain
            
            # Update the global maximum sum if the new path is better
            self.max_sum = max(self.max_sum, price_newpath)
            
            # For recursion return the maximum gain if continue the same path
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum
