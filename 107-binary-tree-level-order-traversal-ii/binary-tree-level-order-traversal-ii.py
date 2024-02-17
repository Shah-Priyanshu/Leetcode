# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        layers = []
        def helper(root, layer, layers):
            if not root:
                return
            if layer + 1 > len(layers):
                layers.append([])
            layers[layer].append(root.val)
            helper(root.left, layer + 1, layers)
            helper(root.right, layer + 1, layers)
        helper(root, 0, layers)
        return layers[::-1]