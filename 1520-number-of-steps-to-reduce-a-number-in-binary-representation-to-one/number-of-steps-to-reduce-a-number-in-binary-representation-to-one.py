class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)
        counter = 0
        while num != 1:
            if num % 2 == 0 :
                num //=2
            else:
                num+=1
            counter+=1
        return counter
        