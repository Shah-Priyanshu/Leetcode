from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        n = len(nums)
        
        if n == 0:
            return result
        
        start = nums[0]
        
        for i in range(1, n):
            # Check if the current number is not consecutive
            if nums[i] != nums[i - 1] + 1:
                # If start and previous number are the same, add "start"
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i - 1]}")
                
                # Update start to the current number
                start = nums[i]
        
        # Handle the last range
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")
        
        return result
