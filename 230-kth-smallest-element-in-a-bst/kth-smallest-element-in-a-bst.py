# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize an empty stack to simulate in-order traversal
        stack = []
        current = root

        # Perform iterative in-order traversal
        while current or stack:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Current is None, process the node on top of the stack
            current = stack.pop()
            k -= 1
            
            # If k is 0, we found the kth smallest element
            if k == 0:
                return current.val
            
            # Go to the right subtree
            current = current.right
        
        return -1  # In case of an invalid input
