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
        dp = {}
        # memoization hashmap: (l, r) : subtree
        def subtree(l, r):
            if (l, r) in dp:
                return dp[(l, r)]
            res = []
            if l == r:
                return [TreeNode(l)]
            if l > r:
                return [None]
            for v in range(l, r+1):
                left_subtree = subtree(l, v-1)
                right_subtree = subtree(v+1, r)
                for lt in left_subtree:
                    for rt in right_subtree:
                        res += [TreeNode(v, lt, rt)]
            dp[(l, r )] = res
            return res
        return subtree(1, n)