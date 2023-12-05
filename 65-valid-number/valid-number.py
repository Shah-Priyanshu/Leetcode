class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            if s.__contains__("inf") or s.__contains__("Infinity") or s=="nan":
                return False
            s = float(s)
            return True
        except:
            return False
        