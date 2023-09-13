class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        # Compute the prefix array for the needle
        def compute_prefix(needle):
            prefix = [0] * len(needle)
            j = 0
            for i in range(1, len(needle)):
                while j > 0 and needle[i] != needle[j]:
                    j = prefix[j - 1]
                if needle[i] == needle[j]:
                    j += 1
                prefix[i] = j
            return prefix

        prefix = compute_prefix(needle)
        j = 0  # Pointer for the needle
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = prefix[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - j + 1

        return -1
