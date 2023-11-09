from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)
        
        for word in strs:
            # Count the occurrences of each character in the word
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            # Convert the count list to a tuple to use it as a dictionary key
            key = tuple(count)
            
            # Check if the key is already in the dictionary
            anagrams[key].append(word)
        
        return list(anagrams.values())
