class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        # Generate the (n-1)-bit Gray code sequence recursively
        prev_gray_code = self.grayCode(n - 1)
        # Add 1 to the front of each number in the previous list in reverse order
        return prev_gray_code + [x + (1 << (n - 1)) for x in reversed(prev_gray_code)]