class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Create a dictionary to store anagrams
        anagrams = defaultdict(list)
        
        # Iterate through each string
        for word in strs:
            # Sort the characters to create a unique key
            # for anagrams that have the same sorted characters
            sorted_word = ''.join(sorted(word))
            
            # Append the word to the list of its anagrams
            anagrams[sorted_word].append(word)
        
        # Convert the values of the dictionary (lists of anagrams) to a list
        result = list(anagrams.values())
        
        return result