class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Index = {}
        for i in range(len(nums)):
            if target - nums[i] in Index:
                return [Index[target - nums[i]], i]
            Index[nums[i]] = i
        return [] 
        