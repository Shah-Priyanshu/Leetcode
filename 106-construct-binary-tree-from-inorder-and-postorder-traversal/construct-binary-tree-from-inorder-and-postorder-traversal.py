class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        # The last element in postorder is the root of the tree
        root = TreeNode(postorder[-1])
        mid = inorder.index(postorder.pop())

        # Build right subtree before left subtree
        root.right = self.buildTree(inorder[mid+1:], postorder)
        root.left = self.buildTree(inorder[:mid], postorder)

        return root
