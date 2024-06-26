# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        def build_balanced_bst(sorted_nodes):
            if not sorted_nodes:
                return None
            mid = len(sorted_nodes) // 2
            root = TreeNode(sorted_nodes[mid])
            root.left = build_balanced_bst(sorted_nodes[:mid])
            root.right = build_balanced_bst(sorted_nodes[mid + 1:])
            return root
        
        # Step 1: Get the sorted array of node values via inorder traversal
        sorted_nodes = inorder_traversal(root)
        
        # Step 2: Build the balanced BST from the sorted array
        return build_balanced_bst(sorted_nodes)
