class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_line(houses: List[int]) -> int:
            if not houses:
                return 0
            if len(houses) == 1:
                return houses[0]
            
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            
            for i in range(2, len(houses)):
                dp[i] = max(dp[i-1], dp[i-2] + houses[i])
            
            return dp[-1]
        
        # Calculate the maximum money by excluding the first house
        exclude_first = rob_line(nums[1:])
        # Calculate the maximum money by excluding the last house
        exclude_last = rob_line(nums[:-1])
        
        # The result is the maximum of the two scenarios
        return max(exclude_first, exclude_last)
