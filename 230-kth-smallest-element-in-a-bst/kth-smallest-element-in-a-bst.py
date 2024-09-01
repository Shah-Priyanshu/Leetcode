# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = -1
        
        def traverse(node):
            nonlocal k, result
            if not node or result != -1:
                return

            traverse(node.left)
            
            k -= 1
            if k == 0:
                result = node.val
                return
            
            traverse(node.right)

        traverse(root)
        return result
