class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
         # Handle special cases for 0 and 1
        if x == 0 or x == 1:
            return x

        # Binary search for the square root
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            mid_squared = mid * mid

            # If the middle value squared is equal to x, return mid
            if mid_squared == x:
                return mid

            # If mid_squared is less than x, search the right half
            elif mid_squared < x:
                left = mid + 1

            # If mid_squared is greater than x, search the left half
            else:
                right = mid - 1

        # When the binary search ends, return the integer part of the last mid
        return right