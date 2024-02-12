# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        # Two stacks to keep track of the current level and the next level nodes
        current_level = [root]
        next_level = []
        
        # List to store the final result
        result = []
        
        # Direction flag: True for left-to-right, False for right-to-left
        left_to_right = True

        while current_level:
            # Temporary list to store the current level's values
            level_values = []
            while current_level:
                # Pop a node from the current level
                node = current_level.pop()
                level_values.append(node.val)
                
                # Based on the traversal direction, push children to the next level stack
                if left_to_right:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                else:
                    if node.right:
                        next_level.append(node.right)
                    if node.left:
                        next_level.append(node.left)
            
            # Add the current level's values to the result
            result.append(level_values)
            # Swap the stacks and change the traversal direction
            current_level, next_level = next_level, []
            left_to_right = not left_to_right
        
        return result
