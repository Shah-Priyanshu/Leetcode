class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        root_val = preorder[0]
        root_idx = inorder_map[root_val]

        left_preorder = preorder[1:root_idx + 1]
        right_preorder = preorder[root_idx + 1:]
        left_inorder = inorder[:root_idx]
        right_inorder = inorder[root_idx + 1:]

        root = TreeNode(root_val)
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root
