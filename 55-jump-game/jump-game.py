class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        last_index = len(nums) - 1
        
        for i in range(last_index):
            if i > max_reach:
                return False
            
            max_reach = max(max_reach, i + nums[i])
            
            # If the maximum reachable index is greater than or equal to the last index, return True.
            if max_reach >= last_index:
                return True
        
        return max_reach >= last_index
