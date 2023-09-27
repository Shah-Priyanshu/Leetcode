class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # Calculate the width between the two vertical lines.
            width = right - left
            # Calculate the minimum height between the two vertical lines.
            min_height = min(height[left], height[right])
            # Calculate the water trapped in this container.
            water = width * min_height
            # Update the maximum water if this container has more water.
            max_water = max(max_water, water)

            # Move the pointers towards each other, trying to find a larger container.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water