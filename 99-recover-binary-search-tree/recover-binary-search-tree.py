# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        x = y = predecessor = pred = None

        while root:
            # If there is a left child, then process the left subtree
            if root.left:
                # Find the rightmost node in the left subtree or the left child itself
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right

                # If the right child of the predecessor is null, then this is the first time we are visiting the left subtree
                if predecessor.right is None:
                    # Set right child of predecessor to the current root to create a back link
                    predecessor.right = root
                    root = root.left
                else:
                    # It means this is the second time we are visiting the node, so cut the link to restore the tree structure
                    if pred and root.val < pred.val:
                        y = root
                        if x is None:
                            x = pred
                    pred = root

                    predecessor.right = None
                    root = root.right
            else:
                # If there is no left child, then just process the current node and move to the right child
                if pred and root.val < pred.val:
                    y = root
                    if x is None:
                        x = pred
                pred = root

                root = root.right

        # Swap the values of the two nodes
        if x and y:
            x.val, y.val = y.val, x.val