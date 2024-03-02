# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        # Helper function to perform DFS
        def dfs(node, currentPath, currentSum):
            if not node:
                return
            
            # Add the current node's value to the path and sum
            currentPath.append(node.val)
            currentSum += node.val
            
            # Check if it's a leaf node and the sum matches targetSum
            if not node.left and not node.right and currentSum == targetSum:
                # Make a deep copy of the path and add it to the results
                result.append(list(currentPath))
            else:
                # Continue the search in the left and right children
                dfs(node.left, currentPath, currentSum)
                dfs(node.right, currentPath, currentSum)
            
            # Backtrack to explore other paths
            currentPath.pop()
        
        result = []
        dfs(root, [], 0)
        return result
