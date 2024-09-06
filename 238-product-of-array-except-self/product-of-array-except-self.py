from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [1] * length
        
        # Step 1: Calculate the prefix product for each element
        prefix = 1
        for i in range(length):
            answer[i] = prefix
            prefix *= nums[i]
        
        # Step 2: Calculate the suffix product for each element and multiply with prefix
        suffix = 1
        for i in range(length - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer
