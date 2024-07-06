import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min-heap with the first k elements
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        
        # Process the remaining elements
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        
        # The root of the heap is the kth largest element
        return min_heap[0]