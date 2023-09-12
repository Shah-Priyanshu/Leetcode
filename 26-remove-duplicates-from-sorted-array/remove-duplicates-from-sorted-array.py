class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Convert the list to a set to remove duplicates and sort it
        nums[:] = sorted(set(nums))
        return len(nums)