class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Initialize the count of non-val elements
        n = len(nums)
        
        for i in range(n):
            if nums[i] != val:
                if i != k:  # Avoid unnecessary assignments when the value is not equal to val
                    nums[k], nums[i] = nums[i], nums[k]  # Swap the elements
                k += 1  # Increment the count of non-val elements
                
        return k