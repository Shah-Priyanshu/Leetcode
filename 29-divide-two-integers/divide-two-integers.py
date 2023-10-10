class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Handle special cases
        if divisor == 0:
            raise ZeroDivisionError("Division by zero")
        if dividend == 0:
            return 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Determine the sign of the result
        negative_result = (dividend < 0) ^ (divisor < 0)

        # Take the absolute values of dividend and divisor
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            dividend -= temp_divisor
            quotient += multiple

        # Adjust the sign of the result
        if negative_result:
            quotient = -quotient

        # Handle overflow cases
        if quotient > INT_MAX:
            return INT_MAX
        elif quotient < INT_MIN:
            return INT_MIN
        else:
            return quotient