class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(segment):
            # Check if the segment is valid:
            # 1. Less than or equal to 255
            # 2. No leading zeros unless the segment is '0'
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

        def backtrack(prev_position=-1, dots=3, path=[]):
            # If we placed all 3 dots, check if the last segment is valid.
            if dots == 0:
                segment = s[prev_position + 1:]
                if isValid(segment):
                    result.append('.'.join(path + [segment]))
                return
            
            # Try placing a dot in all possible positions after prev_position
            for i in range(prev_position + 1, min(len(s) - 1, prev_position + 4)):
                segment = s[prev_position + 1:i + 1]
                if isValid(segment):
                    backtrack(i, dots - 1, path + [segment])

        result = []
        backtrack()
        return result
