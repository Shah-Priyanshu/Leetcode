from itertools import combinations

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = []
        n = len(nums)

        for k in range(n + 1):
            subsets.extend(combinations(nums, k))

        return [list(subset) for subset in subsets]