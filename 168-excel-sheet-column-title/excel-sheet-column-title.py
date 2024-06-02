class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1  # Adjust columnNumber to be zero-indexed
            result.append(chr(columnNumber % 26 + ord('A')))
            columnNumber //= 26
        result.reverse()  # The result is built in reverse order
        return ''.join(result)