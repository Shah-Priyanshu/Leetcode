class Solution(object):
    def minimumTotal(self, triangle):
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update the current value based on the minimum path
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        return triangle[0][0]
        