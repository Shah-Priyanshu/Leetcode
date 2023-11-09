class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        
        for word in strs:
            # Initialize a count array for characters 'a' to 'z'
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            # Convert the count list to a tuple to use it as a dictionary key
            key = tuple(count)
            
            # Check if the key is already in the dictionary
            if key in anagrams:
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        
        return list(anagrams.values())
