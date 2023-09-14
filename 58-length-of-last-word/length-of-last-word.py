class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Remove trailing spaces from the end of the string
        s = s.rstrip()
        
        # Split the string by spaces to get a list of words
        words = s.split(' ')
        
        # Check if there are any words in the list
        if len(words) == 0:
            return 0
        
        # Return the length of the last word in the list
        return len(words[-1])       