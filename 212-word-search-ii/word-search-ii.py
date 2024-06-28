class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word

    def delete(self, word):
        def _delete(node, word, depth):
            if not node:
                return False

            if depth == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False

                return len(node.children) == 0

            char = word[depth]
            if _delete(node.children.get(char), word, depth + 1):
                del node.children[char]
                return not node.is_end_of_word and len(node.children) == 0

            return False

        _delete(self.root, word, 0)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node, i, j, visited):
            if node.is_end_of_word:
                result.add(node.word)
                trie.delete(node.word)
                node.is_end_of_word = False  # Avoid duplicate additions

            char = board[i][j]
            visited.add((i, j))
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and (x, y) not in visited and board[x][y] in node.children:
                    dfs(node.children[board[x][y]], x, y, visited)
            visited.remove((i, j))

        # Build Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.root.children:
                    dfs(trie.root.children[board[i][j]], i, j, set())
        
        return list(result)
