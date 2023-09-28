class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the input array in ascending order.
        triplets = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates to avoid duplicate triplets.
            
            left, right = i + 1, len(nums) - 1  # Initialize two pointers.
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  # Skip duplicates on the left.
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  # Skip duplicates on the right.
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return triplets