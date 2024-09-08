from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Initialize the result list and a deque to store indices
        result = []
        deq = deque()
        
        # Iterate through the array
        for i in range(len(nums)):
            # Remove elements from the back of the deque if they are less than the current element
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()
            
            # Append the current index to the deque
            deq.append(i)
            
            # Remove the front element if it is out of the window
            if deq[0] == i - k:
                deq.popleft()
            
            # Append the maximum value (at the front of the deque) to the result list
            if i >= k - 1:
                result.append(nums[deq[0]])
        
        return result
