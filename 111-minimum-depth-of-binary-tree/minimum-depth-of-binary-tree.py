class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Base case: empty tree
        if not root:
            return 0

        # Handle leaves directly
        if not root.left and not root.right:
            return 1

        # Recursive case: minimum depth from either child
        left_depth = float('inf') if not root.left else self.minDepth(root.left)
        right_depth = float('inf') if not root.right else self.minDepth(root.right)

        # Minimum depth is 1 + min(left_depth, right_depth)
        return 1 + min(left_depth, right_depth)
