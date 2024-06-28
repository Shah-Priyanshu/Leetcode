class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        stack = [(self.root, 0)]
        
        while stack:
            node, index = stack.pop()
            if index == len(word):
                if node.is_end_of_word:
                    return True
                continue
            
            char = word[index]
            if char == '.':
                for child in node.children.values():
                    stack.append((child, index + 1))
            else:
                if char in node.children:
                    stack.append((node.children[char], index + 1))
                    
        return False