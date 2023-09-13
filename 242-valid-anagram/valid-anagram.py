class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        char_count = {}  # Dictionary to count character frequencies

        # Count character frequencies in s and update the dictionary
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        # Decrement character frequencies in t and check if they go negative
        for char in t:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] < 0:
                    return False
            else:
                return False

        return True