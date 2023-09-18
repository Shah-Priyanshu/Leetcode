class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        r=1
        for i in range(n):
            store=a
            a=r
            r=store+r
            
        return r