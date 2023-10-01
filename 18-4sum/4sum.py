class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array in ascending order
        quadruplets = []
        
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for i
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue  # Skip duplicates for j
                left, right = j + 1, len(nums) - 1  # Initialize two pointers
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        # Skip duplicates for left and right
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return quadruplets