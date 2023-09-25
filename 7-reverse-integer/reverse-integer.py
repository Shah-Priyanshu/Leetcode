class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define the maximum and minimum 32-bit integer values
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Initialize the result
        result = 0

        # Handle negative numbers
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1

        while x != 0:
            # Extract the last digit of x
            digit = x % 10

            # Check for integer overflow
            if result > (INT_MAX - digit) // 10:
                return 0

            # Add the digit to the result
            result = result * 10 + digit

            # Remove the last digit from x
            x //= 10

        return result * sign
