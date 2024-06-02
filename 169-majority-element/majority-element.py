class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        # Phase 1: Find a candidate
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        # Phase 2: Verify the candidate
        count = 0
        for num in nums:
            if num == candidate:
                count += 1

        if count > len(nums) // 2:
            return candidate
        else:
            return None
    