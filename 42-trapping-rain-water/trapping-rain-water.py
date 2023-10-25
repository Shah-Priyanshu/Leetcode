class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        out = 0
        n = len(height)
        if n == 0:
            return 0
        left = 0
        right = n - 1
        lmax = height[0]
        rmax = height[-1]
        while left < right:
            if height[left] < height[right]:
                if height[left] < lmax:
                    out += lmax - height[left]
                else:
                    lmax = height[left]
                left += 1
            else:
                if height[right] < rmax:
                    out += rmax - height[right]
                else:
                    rmax = height[right]
                right -= 1
        return out