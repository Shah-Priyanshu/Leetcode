class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Initialize pointers and count
        write_idx = 1
        count = 1

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1  # Reset count for new unique element

            # Copy the element if count is less than or equal to 2
            if count <= 2:
                if write_idx != i:
                    nums[write_idx] = nums[i]
                write_idx += 1

        return write_idx