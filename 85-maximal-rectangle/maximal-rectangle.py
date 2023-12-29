class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0

            max_area = max(max_area, self.largestRectangleArea(heights))

        return max_area

    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        width = [0] * len(heights)

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                top = stack.pop()
                height = heights[top]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * w)

            stack.append(i)
            width[i] = i if not stack else i - stack[-1]

        while stack:
            top = stack.pop()
            height = heights[top]
            w = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, height * w)

        return max_area