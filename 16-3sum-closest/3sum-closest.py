class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()  # Sort the input array in ascending order
        closest_sum = float('inf')  # Initialize closest_sum to positive infinity

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1  # Initialize two pointers
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum == target:
                    return current_sum  # Found an exact match, return it
                
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum  # Update closest_sum if the current sum is closer to the target
                
                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum