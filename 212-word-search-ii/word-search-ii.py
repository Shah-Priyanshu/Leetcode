class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def remove(self, word):
        def _remove(node, word, depth):
            if depth == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            char = word[depth]
            if char not in node.children:
                return False
            should_delete = _remove(node.children[char], word, depth + 1)
            if should_delete:
                del node.children[char]
                return len(node.children) == 0
            return False

        _remove(self.root, word, 0)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node, i, j, path):
            char = board[i][j]
            next_node = node.children.get(char)
            if not next_node:
                return

            path.append(char)
            board[i][j] = '#'  # Mark as visited

            if next_node.is_end_of_word:
                found_word = ''.join(path)
                result.add(found_word)
                trie.remove(found_word)
                next_node.is_end_of_word = False  # Avoid duplicate additions

            # Explore neighbors
            for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != '#':
                    dfs(next_node, x, y, path)

            board[i][j] = char  # Unmark as visited
            path.pop()

        # Build Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.root.children:
                    dfs(trie.root, i, j, [])

        return list(result)
