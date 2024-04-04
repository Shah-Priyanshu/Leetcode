from collections import defaultdict

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        def gcd(a, b):
            """Compute the Greatest Common Divisor of a and b."""
            while b:
                a, b = b, a % b
            return a

        def get_slope(x1, y1, x2, y2):
            """Calculate and return the slope in reduced form as a tuple (dx, dy)."""
            dx, dy = x2 - x1, y2 - y1
            if dx == 0:  # Vertical line
                return (0, 1)
            if dy == 0:  # Horizontal line
                return (1, 0)
            g = gcd(dx, dy)
            return (dx // g, dy // g)

        if len(points) <= 2:
            return len(points)

        max_points = 0
        for i in range(len(points)):
            slope_count = defaultdict(int)
            same_points = 1  # Count the point itself
            local_max = 0
            for j in range(i + 1, len(points)):
                if points[i] == points[j]:
                    same_points += 1  # Handle overlapping points
                else:
                    slope = get_slope(points[i][0], points[i][1], points[j][0], points[j][1])
                    slope_count[slope] += 1
                    local_max = max(local_max, slope_count[slope])
            max_points = max(max_points, local_max + same_points)

        return max_points