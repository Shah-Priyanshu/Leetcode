class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        multiplier = 1
        if len(s) == 0:
            return 0
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            multiplier = -1
            s = s[1:]
        arr = deque()
        for i in s:
            if i.isdigit():
                arr.appendleft(int(i))
            else:
                break
        place = 1
        ret = 0
        while(len(arr) > 0):
            ret = ret + place * arr.popleft()
            place = place * 10
        if ret >= 2147483648:
            if multiplier == 1:
                return 2147483647
            else:
                return -2147483648
        else:
            return ret * multiplier