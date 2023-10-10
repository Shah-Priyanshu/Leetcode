class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Handle edge cases
        if dividend == 0:
            return 0
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Determine the sign of the result
        positive_result = (dividend < 0) == (divisor < 0)
        
        # Take the absolute values of dividend and divisor
        dividend, divisor = abs(dividend), abs(divisor)
        
        quotient = 0
        while dividend >= divisor:
            # Initialize variables for the current subtraction loop
            temp_divisor = divisor
            temp_quotient = 1
            
            # Keep doubling the temp_divisor and temp_quotient
            # until it's larger than dividend
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                temp_quotient <<= 1
            
            # Subtract temp_divisor from dividend and add temp_quotient to the result
            dividend -= temp_divisor
            quotient += temp_quotient
        
        # Adjust the sign of the result
        return quotient if positive_result else -quotient