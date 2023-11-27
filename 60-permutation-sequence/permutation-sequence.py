class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = list(range(1, n + 1))
        permutation = []
        k -= 1  # Convert k to zero-based index

        # Calculate factorial of n-1
        factorial = 1
        for i in range(1, n):
            factorial *= i

        # Determine each digit
        for i in range(n - 1, 0, -1):
            index = k // factorial
            k %= factorial
            permutation.append(numbers.pop(index))

            factorial //= i

        # Add the last number
        permutation.append(numbers[0])

        # Convert list of numbers to a string
        return ''.join(map(str, permutation))