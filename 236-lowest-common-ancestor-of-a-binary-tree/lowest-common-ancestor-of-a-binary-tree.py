# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if the current node is None or matches either p or q
        if root is None or root == p or root == q:
            return root

        # Recursively find LCA in the left subtree
        left = self.lowestCommonAncestor(root.left, p, q)
        # Recursively find LCA in the right subtree
        right = self.lowestCommonAncestor(root.right, p, q)

        # If both left and right are non-None, root is the LCA
        if left and right:
            return root

        # If either left or right is the LCA, return it
        return left if left else right
