class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove leading whitespace
        s = s.lstrip()

        # Check if the string is empty after removing whitespace
        if not s:
            return 0

        # Check for the sign (positive or negative)
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # Initialize the result
        result = 0

        # Iterate through the characters and convert to integer
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        # Apply the sign
        result *= sign

        # Clamp the result to the 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result
