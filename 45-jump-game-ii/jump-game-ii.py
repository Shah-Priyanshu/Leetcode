class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n == 1:
            return 0

        max_reach = nums[0]  # Maximum reachable index after the current jump
        steps = nums[0]  # Number of steps in the current jump
        jumps = 1  # Number of jumps needed

        for i in range(1, n):
            if i == n - 1:
                return jumps

            max_reach = max(max_reach, i + nums[i])
            steps -= 1

            if steps == 0:
                jumps += 1
                steps = max_reach - i

        return 0  # This should not be reached since it's guaranteed that you can reach the end

