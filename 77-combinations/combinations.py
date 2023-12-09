class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        combinations = []
        nums = list(range(1, k + 1))

        while nums[0] <= n - k + 1:
            combinations.append(nums[:])
            i = k - 1
            while i >= 0 and nums[i] == n - k + 1 + i:
                i -= 1

            if i >= 0:
                nums[i] += 1
                for j in range(i + 1, k):
                    nums[j] = nums[j - 1] + 1
            else:
                break

        return combinations