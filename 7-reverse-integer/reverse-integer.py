class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        final = 0
            
        negative = False
        if x < 0:
            negative = True
            x = abs(x)

        stringX = str(x)[::-1]
        backwards = int(stringX)
        #digits = [int(i) for i in stringX]

        if negative == True:
            final = backwards*-1
        else:
            final = backwards

        if final > (2**31 - 1) or final < (-1*(2**31)):
            final = 0
        
        return final