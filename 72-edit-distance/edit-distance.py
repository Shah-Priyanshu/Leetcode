class Solution(object):
    from collections import deque
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1)
        l2 = len(word2)

        if word1 == word2:
            return 0
        elif not word1 or not word2:
            return max(l1, l2)

        num = 0
        visited = set()
        q = deque()
        q.append((0, 0))

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                if (i, j) in visited:
                    continue
                
                visited.add((i, j))
                while i < l1 and j < l2 and word1[i] == word2[j]:
                    i += 1
                    j += 1
                if i == l1 and j == l2:
                    return num
                q.append((i + 1, j))
                q.append((i, j + 1))
                q.append((i + 1, j + 1))
            num += 1