class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(array, index):

            if index == len(nums):
                return

            for i in range(index, len(nums)):
                array.append(nums[i])
                res.append(array[:])
                dfs(array[:], i+1) 
                array.pop()
 
        res = [[]]
        dfs([], 0)
        return res