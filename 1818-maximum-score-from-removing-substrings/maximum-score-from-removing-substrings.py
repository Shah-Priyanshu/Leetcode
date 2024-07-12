class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substring(s, first, second, value):
            stack = []
            points = 0
            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    points += value
                else:
                    stack.append(char)
            return ''.join(stack), points
        
        if x > y:
            # Prioritize removing "ab" first
            s, points = remove_substring(s, 'a', 'b', x)
            _, points2 = remove_substring(s, 'b', 'a', y)
        else:
            # Prioritize removing "ba" first
            s, points = remove_substring(s, 'b', 'a', y)
            _, points2 = remove_substring(s, 'a', 'b', x)
        
        return points + points2
