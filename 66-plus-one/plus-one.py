class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res=0
        for i in digits:
            res=res*10+i
        res=res+1
        return [int(digit) for digit in str(res)]