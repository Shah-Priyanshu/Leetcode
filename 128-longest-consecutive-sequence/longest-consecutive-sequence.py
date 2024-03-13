class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)  # Store numbers in a set for O(1) look-up
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:  # Check if 'num' is the start of a sequence
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:  # Check consecutive numbers
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)  # Update longest streak

        return longest_streak
