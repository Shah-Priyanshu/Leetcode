class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        
        buckets = {}
        bucket_size = valueDiff + 1
        
        for i, num in enumerate(nums):
            bucket_id = num // bucket_size
            
            # Check the current bucket
            if bucket_id in buckets:
                return True
            
            # Check the previous bucket
            if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
            
            # Check the next bucket
            if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
            
            # Add the current number to the bucket
            buckets[bucket_id] = num
            
            # Maintain the window size
            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // bucket_size
                del buckets[old_bucket_id]
        
        return False
