class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        # Reverse the string
        rev_s = s[::-1]

        # Create the combined string with a special character in between
        combined = s + "#" + rev_s

        # Function to compute the LPS array using the KMP algorithm
        def computeLPS(pattern: str) -> [int]:
            lps = [0] * len(pattern)
            length = 0
            i = 1
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        # Compute the LPS array for the combined string
        lps = computeLPS(combined)

        # The length of the longest palindromic prefix
        longest_palindromic_prefix_len = lps[-1]

        # Characters to add in front of the original string
        chars_to_add = rev_s[:len(s) - longest_palindromic_prefix_len]

        # Form the result
        result = chars_to_add + s

        return result