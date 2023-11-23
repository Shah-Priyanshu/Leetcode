class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
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
        # binary search to find insertion point
        
        # binary search by the end value to find the first interval which overlaps with the insertion's start value
        # find the first end value which is less than the insertion's start value. Add one to this index and this is the first array to consider. They overlap if the starting value of the found interval is less than or equal to the end value of the insertion.

        # binary search by the start value to find the last interval which overlaps with the insertion's end value
        # find the first start value which is greater than the insertion's end value. remove one from this index. We now have an interval which contains a start value guaranteed to be less than or equal to the insertion's end value. They overlap if the insertion's start value is less than or equal to the found interval's end value.
        if len(intervals) == 0:
            return [newInterval]
        l, r = int(math.ceil(binSearch(newInterval[0], 1))), int(math.floor(binSearch(newInterval[1], 0)))
        if l == len(intervals):
            return intervals + [newInterval]
        if r == -1:
            return [newInterval] + intervals
        if intervals[l][0] <= newInterval[1]:
            li = True
        else:
            li = False
        
        if newInterval[0] <= intervals[r][1]:
            ri = True
        else:
            ri = False
        
        if ri and li:
            return intervals[:l] + [[min(newInterval[0], intervals[l][0]), max(newInterval[1], intervals[r][1])]] + intervals[r + 1:]
        if li:
            return intervals[:l] + [[min(newInterval[0], intervals[l][0]), newInterval[1]]] + intervals[r:]
        if ri:
            return intervals[:l+1] + [[newInterval[0], max(newInterval[1], intervals[r][1])]] + intervals[r+1:]
        return intervals[:l] + [newInterval] + intervals[r+1:]    