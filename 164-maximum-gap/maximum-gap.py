from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # Handle edge case where there are fewer than two elements
        if len(nums) < 2:
            return 0
        
        # Find the minimum and maximum elements
        min_val, max_val = float('inf'), float('-inf')
        for num in nums:
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num
        
        # If all numbers are the same, the max gap is 0
        if min_val == max_val:
            return 0
        
        # Calculate the bucket size and number of buckets
        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))  # At least one element per bucket
        bucket_count = (max_val - min_val) // bucket_size + 1
        
        # Initialize buckets
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]
        
        # Distribute the numbers into the buckets
        for num in nums:
            index = (num - min_val) // bucket_size
            buckets[index][0] = min(buckets[index][0], num)
            buckets[index][1] = max(buckets[index][1], num)
        
        # Calculate the maximum gap
        max_gap = 0
        prev_max = min_val
        
        for i in range(bucket_count):
            if buckets[i][0] == float('inf') and buckets[i][1] == float('-inf'):
                continue  # Skip empty buckets
            current_min = buckets[i][0]
            max_gap = max(max_gap, current_min - prev_max)
            prev_max = buckets[i][1]
        
        return max_gap