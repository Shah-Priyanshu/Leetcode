class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math

        nums = [str(i) for i in range(1, n+1)]
        result = []

        k -= 1

        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            result.append(nums[index])
            nums.remove(nums[index])

        return ''.join(result)