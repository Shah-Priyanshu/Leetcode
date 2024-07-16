# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find_path(node, target):
            if not node:
                return None
            if node.val == target:
                return ""
            left_path = find_path(node.left, target)
            if left_path is not None:
                return "L" + left_path
            right_path = find_path(node.right, target)
            if right_path is not None:
                return "R" + right_path
            return None
        
        def find_lca(node, p, q):
            if not node or node.val == p or node.val == q:
                return node
            left = find_lca(node.left, p, q)
            right = find_lca(node.right, p, q)
            if left and right:
                return node
            return left if left else right
        
        # Step 1: Find the LCA of startValue and destValue
        lca = find_lca(root, startValue, destValue)
        
        # Step 2: Find the path from LCA to startValue and destValue
        path_to_start = find_path(lca, startValue)
        path_to_dest = find_path(lca, destValue)
        
        # Step 3: Convert path_to_start to all 'U's and append path_to_dest
        result = 'U' * len(path_to_start) + path_to_dest
        return result
