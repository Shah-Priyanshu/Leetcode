class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        nums.sort()
        n = len(nums)
        
        # Possible cases after at most 3 moves
        case1 = nums[n-1] - nums[3]   # Remove the 3 smallest elements
        case2 = nums[n-2] - nums[2]   # Remove the 2 smallest and the largest element
        case3 = nums[n-3] - nums[1]   # Remove the smallest and the 2 largest elements
        case4 = nums[n-4] - nums[0]   # Remove the 3 largest elements
        
        # The result is the minimum difference from the possible cases
        return min(case1, case2, case3, case4)
