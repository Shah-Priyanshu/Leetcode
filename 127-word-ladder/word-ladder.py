class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        wordList = set(wordList)
        beginSet, endSet = {beginWord}, {endWord}
        wordLength = len(beginWord)
        length = 1

        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet  # Swap to always expand the smaller set

            nextSet = set()
            for word in beginSet:
                for i in range(wordLength):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nextWord = word[:i] + c + word[i+1:]
                        if nextWord in endSet:
                            return length + 1
                        if nextWord in wordList:
                            nextSet.add(nextWord)
                            wordList.remove(nextWord)
            beginSet = nextSet
            length += 1

        return 0
