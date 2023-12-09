class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""

        target_counts = [0] * 128
        for char in t:
            target_counts[ord(char)] += 1

        required_chars = sum(1 for count in target_counts if count > 0)
        formed_chars = 0

        left, right = 0, 0
        min_len = float('inf')
        min_window_start = 0

        while right < len(s):
            # Expand the window to the right
            target_counts[ord(s[right])] -= 1
            if target_counts[ord(s[right])] == 0:
                formed_chars += 1

            # Try to contract the window from the left
            while formed_chars == required_chars:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window_start = left

                # Update the character count and formed_chars
                target_counts[ord(s[left])] += 1
                if target_counts[ord(s[left])] > 0:
                    formed_chars -= 1

                left += 1

            # Expand the window to the right
            right += 1

        return "" if min_len == float('inf') else s[min_window_start:min_window_start + min_len]