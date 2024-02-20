# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def checkHeight(node):
            # Base case: empty tree is balanced
            if node is None:
                return 0

            # Check the height of the left subtree
            left_height = checkHeight(node.left)
            if left_height == -1:
                return -1  # Left subtree is not balanced

            # Check the height of the right subtree
            right_height = checkHeight(node.right)
            if right_height == -1:
                return -1  # Right subtree is not balanced

            # Check if current node is balanced
            if abs(left_height - right_height) > 1:
                return -1  # Current node is not balanced

            # Return height of the current node
            return max(left_height, right_height) + 1

        # Tree is balanced if checkHeight doesn't return -1
        return checkHeight(root) != -1
