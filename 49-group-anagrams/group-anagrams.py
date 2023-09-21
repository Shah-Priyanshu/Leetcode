class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        
        for word in strs:
            # Calculate a hash value
            count = [0] * 26  # Assuming lowercase English letters
            for char in word:
                count[ord(char) - ord('a')] += 1
            hash_value = tuple(count)
            
            # Append the word to the list of anagrams with the same hash value
            if hash_value in anagrams:
                anagrams[hash_value].append(word)
            else:
                anagrams[hash_value] = [word]
        
        return list(anagrams.values())