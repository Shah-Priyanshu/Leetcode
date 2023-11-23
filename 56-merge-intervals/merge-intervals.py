class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        merged_intervals = [intervals[0]]

        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]
            last_merged_start, last_merged_end = merged_intervals[-1]

            # Check for overlapping intervals
            if current_start <= last_merged_end:
                # Merge the overlapping intervals
                merged_intervals[-1] = [last_merged_start, max(last_merged_end, current_end)]
            else:
                # No overlap, add the current interval to the result
                merged_intervals.append([current_start, current_end])

        return merged_intervals
