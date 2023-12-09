class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        combinations = []
        self.search(nums, 0, [], combinations)
        return combinations

    def search(self, nums, index, subset, combinations):
        combinations.append(list(subset))

        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.search(nums, i + 1, subset, combinations)
            subset.pop()

        