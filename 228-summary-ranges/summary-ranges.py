class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result

        start = nums[0]
        
        for i in range(1, len(nums)):
            # Check if the current number is not consecutive
            if nums[i] != nums[i-1] + 1:
                # If it is a single number range
                if start == nums[i-1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i-1]}")
                # Start a new range
                start = nums[i]
        
        # Add the last range
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(f"{start}->{nums[-1]}")
        
        return result
