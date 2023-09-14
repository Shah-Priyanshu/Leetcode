class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        ## Initialize a variable to keep track of the length of the last word
        length = 0
        
        # Flag to track if we've encountered the last word
        last_word_found = False
        
        # Start from the end of the string and move left
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                length += 1
                last_word_found = True
            elif last_word_found:
                # If we've already encountered the last word and found a space, break
                break
        
        return length     