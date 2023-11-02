class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        sol = []
        
        def dfs(done, todo):
            if len(todo) == 0:
                sol.append(done)
                return

            for i in range(len(todo)):
                dfs(done + [todo[i]], todo[0:i] + todo[i+1:])

        for i in range(len(nums)):
            dfs([nums[i]], nums[0:i] + nums[i+1:])

        return sol