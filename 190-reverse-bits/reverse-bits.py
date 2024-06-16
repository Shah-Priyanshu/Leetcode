class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Extract the bit at position i from n
            bit = (n >> i) & 1
            # Set the bit at position (31 - i) in result
            result = result | (bit << (31 - i))
        return result