class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = list(range(1, n+1))
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            numbers.remove(numbers[index])
        return permutation