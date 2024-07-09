class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}  # Dictionary to store the last seen index of each element
        
        for i, num in enumerate(nums):
            if num in index_map and i - index_map[num] <= k:
                return True
            index_map[num] = i  # Update the last seen index of the current element
        
        return False  # No duplicates found within the given range
