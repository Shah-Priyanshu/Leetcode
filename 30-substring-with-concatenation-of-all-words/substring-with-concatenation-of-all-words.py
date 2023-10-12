from collections import Counter

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words:
            return []
        k = len(words[0])
        res = []
        for left in range(k):
            d = Counter()
            for right in range(left + k, len(s) + 1, k):
                word = s[right - k:right]
                d[word] += 1
                while d[word] > words.count(word):
                    d[s[left:left + k]] -= 1
                    left += k
                if right - left == len(words) * k:
                    res.append(left)
        return res
