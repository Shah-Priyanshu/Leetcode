class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        n = len(s)
        cycle_len = 2 * numRows - 2
        result = []
        
        for i in range(numRows):
            for j in range(i, n, cycle_len):
                result.append(s[j])
                if i != 0 and i != numRows - 1 and j + cycle_len - 2 * i < n:
                    result.append(s[j + cycle_len - 2 * i])

        return ''.join(result)