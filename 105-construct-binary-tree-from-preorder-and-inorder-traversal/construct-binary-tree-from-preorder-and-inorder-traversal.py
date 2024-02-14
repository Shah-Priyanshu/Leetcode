# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        key_map = {v:i for i, v in enumerate(inorder)}

        def helper(l, r):
            if l > r:
                return None
            root = TreeNode(preorder.pop(0))
            idx = key_map[root.val]
            root.left = helper(l, idx - 1)
            root.right = helper(idx + 1, r)
            return root
        
        return helper(0, len(inorder) - 1)