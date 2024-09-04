# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Traverse the tree starting from the root
        current = root

        while current:
            # If both p and q are smaller than current, move to the left child
            if p.val < current.val and q.val < current.val:
                current = current.left
            # If both p and q are greater than current, move to the right child
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                # We have found the split point, so this is the LCA
                return current
