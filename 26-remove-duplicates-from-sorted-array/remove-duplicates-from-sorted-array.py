class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # Initialize a pointer for unique elements
        unique_ptr = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_ptr]:
                unique_ptr += 1
                nums[unique_ptr] = nums[i]
        
        # unique_ptr now points to the last unique element
        # The count of unique elements is unique_ptr + 1
        return unique_ptr + 1