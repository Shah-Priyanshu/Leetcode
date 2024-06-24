class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_diff = [0] * (n + 1)  # Difference array to track flips
        flips = 0  # Number of flips performed
        curr_flips = 0  # Current number of active flips

        for i in range(n):
            curr_flips += flip_diff[i]  # Update current flip state
            if curr_flips % 2 == nums[i]:
                if i + k > n:
                    return -1
                flips += 1
                curr_flips += 1
                flip_diff[i] += 1
                flip_diff[i + k] -= 1

        return flips
