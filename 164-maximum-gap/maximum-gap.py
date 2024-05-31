from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # Handle edge case where there are fewer than two elements
        if len(nums) < 2:
            return 0
        
        # Sort the array and remove duplicates
        nums = sorted(set(nums))
        
        # Initialize the maximum gap
        max_gap = 0
        
        # Compute the maximum gap between successive elements
        for i in range(1, len(nums)):
            current_gap = nums[i] - nums[i - 1]
            if current_gap > max_gap:
                max_gap = current_gap
        
        return max_gap