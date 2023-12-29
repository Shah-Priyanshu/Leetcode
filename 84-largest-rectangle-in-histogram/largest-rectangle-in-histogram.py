class Solution(object):
    def largestRectangleArea(self, heights):
        res = 0
        s = [] # store tuple of index, height
        for i, rect in enumerate(heights):
            if not s:
                s.append((0, rect))
            if rect == s[-1][1]:
                continue
            elif rect > s[-1][1]:
                s.append((i, rect))
                continue
            else:
                ind, height = s.pop()
                res = max(res, height * (i - ind))
                while s and rect < s[-1][1]:
                    ind, height = s.pop()
                    res = max(res, height * (i - ind))
                if not s:
                    s.append((0, rect))
                else:
                    s.append((ind, rect))
        for ind, height in s:
            res = max(res, height * (len(heights) - ind))
        return res