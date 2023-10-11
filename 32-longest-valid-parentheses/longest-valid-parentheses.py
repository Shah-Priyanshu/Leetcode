class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return 0

        temp = 0
        count = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == ')':
                    temp = i - 1 - count[i-1]
                    if temp >= 0 and s[temp] == '(':
                        count[i] = count[i-1] + 2 + (count[temp-1] if temp-1 >= 0 else 0)
                else:
                    count[i] = count[i-2] + 2

                #if previou < count[i]:
                    #previou = count[i]
        #print(count)
        return max(count)