class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n <1 or n > 16:
            return [0]
        prev_gray_code = self.grayCode(n - 1)
        size = 1<<(n - 1)
        current_gray_code = prev_gray_code + [size + i for i in reversed(prev_gray_code)]
        return current_gray_code