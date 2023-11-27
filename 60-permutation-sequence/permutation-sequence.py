class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Factorial function to calculate n!
        def factorial(num):
            result = 1
            for i in range(1, num + 1):
                result *= i
            return result

        # List to store digits available for permutation
        digits = [str(i) for i in range(1, n + 1)]

        # Initialize result string
        result = ''

        # Decrement k to match list indexing
        k -= 1

        # Iterate through each digit in the range [1, n]
        for i in range(1, n + 1):
            # Calculate the index of the current digit in the available digits
            index = k // factorial(n - i)
            # Update k for the next iteration
            k %= factorial(n - i)
            # Append the selected digit to the result
            result += digits.pop(index)

        return result