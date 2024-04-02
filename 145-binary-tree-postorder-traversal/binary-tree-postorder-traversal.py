# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.helper(root, result)
        return result

    def helper(self, node, result):
        if node:
            # Traverse the left subtree
            self.helper(node.left, result)
            # Traverse the right subtree
            self.helper(node.right, result)
            # Visit the node itself (add its value to the result)
            result.append(node.val)