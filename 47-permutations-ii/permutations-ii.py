class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start=0):
            # If we're at the end of the list, we have a complete permutation
            if start == len(nums):
                ans.append(nums[:])
                return
            
            # Use a set to avoid processing duplicates
            seen = set()
            for i in range(start, len(nums)):
                # If number has been used for this position before, skip it
                if nums[i] in seen:
                    continue
                seen.add(nums[i])
                
                # Swap the number at 'start' with the number at 'i'
                nums[start], nums[i] = nums[i], nums[start]
                
                # Recurse for the next position
                backtrack(start + 1)
                
                # Swap back to restore original list state
                nums[start], nums[i] = nums[i], nums[start]

        nums.sort()
        ans = []
        backtrack()
        return ans
