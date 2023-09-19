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
        
        # Base case: If one tree is empty while the other is not, they are not the same.
        if p is None or q is None:
            return False
        
        # Check if the current nodes have the same value.
        if p.val != q.val:
            return False
        
        # Recursively check the left and right subtrees.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)