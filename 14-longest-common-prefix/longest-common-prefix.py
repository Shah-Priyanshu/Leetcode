class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""  # If the input list is empty, return an empty string

        # Find the shortest string in the list
        min_len = min(len(s) for s in strs)

        # Iterate through the characters of the shortest string
        for i in range(min_len):
            # Compare the current character in all strings
            char = strs[0][i]
            for string in strs:
                if string[i] != char:
                    return strs[0][:i]  # Return the common prefix found so far

        return strs[0][:min_len]  # If no mismatch found, return the shortest string
