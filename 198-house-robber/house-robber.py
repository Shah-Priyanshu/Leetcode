class Solution:
    def rob(self, nums: List[int]) -> int:
        # Step 1: Handle edge cases
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Step 2: Initialize the dp array
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        # Step 3: Fill the dp array using the recurrence relation
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        # Step 4: Return the maximum amount that can be robbed
        return dp[len(nums) - 1]
