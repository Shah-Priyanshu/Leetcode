class Solution:
    def hammingWeight(self, n: int) -> int:
        binary_representation = bin(n)[2:]
        count_of_ones = 0
        for bit in binary_representation:
            if bit == '1':
                count_of_ones += 1
        return count_of_ones
