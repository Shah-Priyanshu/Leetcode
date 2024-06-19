class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Initialize shift counter
        shift = 0
        
        # Find the common prefix
        while left < right:
            left = left >> 1
            right = right >> 1
            shift += 1
        
        # Left-shift the common prefix back to its original position
        return left << shift
