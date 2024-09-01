from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        n = len(nums)
        
        if n == 0:
            return result
        
        start = 0  # Start index of a range
        
        for i in range(1, n + 1):
            # Check if we have reached the end of the array or found a break in the consecutive numbers
            if i == n or nums[i] != nums[i - 1] + 1:
                # Add the range to the result
                if start == i - 1:
                    result.append(str(nums[start]))
                else:
                    result.append(f"{nums[start]}->{nums[i - 1]}")
                # Update start to the current number
                start = i
        
        return result
