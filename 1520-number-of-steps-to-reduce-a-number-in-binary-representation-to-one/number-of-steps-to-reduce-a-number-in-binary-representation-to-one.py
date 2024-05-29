class Solution:
    def numSteps(self, s):
        num = int(s, 2)
        counter = 0
        while num != 1:
            if num % 2 == 0: #num is even
                num //=2
            else:
                num+=1
            counter+=1
        return counter
        