import math

class Solution(object):
    def insert(self, intervals, newInterval):
        def binSearch(val, i):
            start = 0
            end = len(intervals) - 1
            while end - start >= 2:
                mid = (start + end) // 2
                if intervals[mid][i] == val:
                    return mid
                if intervals[mid][i] < val:
                    start = mid + 1
                else:
                    end = mid - 1
            if end == start:
                if intervals[end][i] == val:
                    return end
                if intervals[end][i] < val:
                    return end + 0.5
                else:
                    return end - 0.5
            if intervals[start][i] == val:
                return start
            if intervals[start][i] > val:
                return start - 0.5
            if intervals[end][i] > val:
                return start + 0.5
            if intervals[end][i] == val:
                return end
            return end + 0.5
        
        if len(intervals) == 0:
            return [newInterval]

        l, r = int(math.ceil(binSearch(newInterval[0], 1))), int(math.floor(binSearch(newInterval[1], 0)))

        if l == len(intervals):
            return intervals + [newInterval]
        if r == -1:
            return [newInterval] + intervals

        merge_start = min(newInterval[0], intervals[l][0]) if l < len(intervals) else newInterval[0]
        merge_end = max(newInterval[1], intervals[r][1]) if r >= 0 else newInterval[1]

        return intervals[:l] + [[merge_start, merge_end]] + intervals[r + 1:]