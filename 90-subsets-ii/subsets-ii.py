class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recurse(nums, index, curr, ret):
            ret.append(curr)
            i = index
            while i < len(nums):
                print(i)
                curr.append(nums[i])
                recurse(nums, i+1, curr[:], ret)
                used = curr.pop()
                while i < len(nums) and nums[i] == used:
                    i += 1

        ret = []
        recurse(sorted(nums), 0, [], ret)
        return ret