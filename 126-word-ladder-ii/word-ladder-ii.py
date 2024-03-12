class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return []
        
        # Adding beginWord for completeness
        wordList = set(wordList)  # Convert list to set for faster lookup
        wordList.add(beginWord)
        
        # Preprocessing: Generic mapping
        neighbors = {}
        for word in wordList:
            for i in range(len(word)):
                generic_form = word[:i] + "*" + word[i+1:]
                if generic_form not in neighbors:
                    neighbors[generic_form] = []
                neighbors[generic_form].append(word)
        
        # BFS variables
        parents = {word: [] for word in wordList}
        level = {word: float('inf') for word in wordList}
        level[beginWord] = 0
        queue = [beginWord]
        found = False
        
        # BFS
        while queue and not found:
            next_level_queue = []
            for word in queue:
                for i in range(len(word)):
                    generic_form = word[:i] + "*" + word[i+1:]
                    for next_word in neighbors.get(generic_form, []):
                        if level[word] + 1 <= level[next_word]:
                            if level[word] + 1 < level[next_word]:
                                level[next_word] = level[word] + 1
                                next_level_queue.append(next_word)
                            parents[next_word].append(word)
                        if next_word == endWord:
                            found = True
            queue = next_level_queue
        
        # Backtracking to build the paths
        def backtrack(word):
            if word == beginWord:
                return [[beginWord]]
            paths = []
            for parent in parents[word]:
                for prev_path in backtrack(parent):
                    paths.append(prev_path + [word])
            return paths
        
        return backtrack(endWord)
