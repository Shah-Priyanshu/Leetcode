# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
         # Base case: If both trees are empty, they are the same.
        if p is None and q is None:
            return True
        # If only one of the nodes is None, they are not identical
        if p is None or q is None:
            return False
        # Check if values are equal and recursively check left and right subtrees
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # Values are not equal, they are not identical
        return False