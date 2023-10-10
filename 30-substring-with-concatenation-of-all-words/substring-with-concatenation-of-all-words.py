class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter, defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word_count = 0

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = len(words) * word_len
        word_count = Counter(words)
        result = []
        trie = TrieNode()

        for word in words:
            node = trie
            for char in word:
                node = node.children[char]
            node.word_count += 1

        for i in range(word_len):
            left, right = i, i
            curr_count = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    curr_count[word] += 1

                    while curr_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        left += word_len
                        curr_count[left_word] -= 1

                    if right - left == total_len:
                        result.append(left)

                else:
                    curr_count.clear()
                    left = right

        return result
