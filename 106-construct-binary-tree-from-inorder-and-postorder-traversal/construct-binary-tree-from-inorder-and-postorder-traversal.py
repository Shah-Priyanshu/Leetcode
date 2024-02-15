class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        # Map of value to its index in inorder array for quick lookup
        in_map = {val: idx for idx, val in enumerate(inorder)}

        def buildTreeHelper(in_start, in_end, post_start, post_end):
            if in_start > in_end or post_start > post_end:
                return None

            # The last element in the current postorder segment is the root
            root_val = postorder[post_end]
            root = TreeNode(root_val)

            # Find the index of the root in inorder array
            in_root_idx = in_map[root_val]

            # Calculate the number of elements in the left subtree
            left_tree_size = in_root_idx - in_start

            # Recursively build the left and right subtrees
            root.left = buildTreeHelper(in_start, in_root_idx - 1, post_start, post_start + left_tree_size - 1)
            root.right = buildTreeHelper(in_root_idx + 1, in_end, post_start + left_tree_size, post_end - 1)

            return root

        return buildTreeHelper(0, len(inorder) - 1, 0, len(postorder) - 1)
