class Solution():
    def wordBreak(self, s, wordDict):
        def backtrack(start, path):
            if start == len(s):
                solutions.append(' '.join(path))
                return
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict:
                    backtrack(end, path + [s[start:end]])
        solutions = []
        backtrack(0, [])
        return solutions