class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0
        while n:
            n &= n - 1  # Remove the lowest set bit
            result += 1    # Increment the count of set bits
        return result
