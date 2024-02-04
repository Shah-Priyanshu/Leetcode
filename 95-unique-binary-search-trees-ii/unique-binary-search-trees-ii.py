# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.generateTreesHelper(1, n)
    
    def generateTreesHelper(self, start, end):
        if start > end:
            return [None]
        
        all_trees = []
        for i in range(start, end + 1):
            # Generate all possible left and right subtrees
            left_trees = self.generateTreesHelper(start, i - 1)
            right_trees = self.generateTreesHelper(i + 1, end)
            
            # Connect left and right trees to the root i
            for l in left_trees:
                for r in right_trees:
                    current_tree = TreeNode(i)
                    current_tree.left = l
                    current_tree.right = r
                    all_trees.append(current_tree)
        
        return all_trees
