class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        # Step 1: Convert all non-positive numbers to n+1
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        # Step 2: Mark elements within the range [1, n] by negating the corresponding index
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        # Step 3: Find the first positive index
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # If all numbers within [1, n] are present, the missing positive is n + 1
        return n + 1
