class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        # Initialize with an initial guess
        guess = x
        while True:
            new_guess = (guess + x // guess) // 2
            if new_guess >= guess:
                return int(guess)
            guess = new_guess