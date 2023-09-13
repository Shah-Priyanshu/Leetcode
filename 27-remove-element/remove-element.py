class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Initialize the count of non-val elements
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move non-val elements to the front of the array
                k += 1  # Increment the count of non-val elements
        return k