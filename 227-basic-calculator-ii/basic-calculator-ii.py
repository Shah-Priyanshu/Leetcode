class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = "+"
        i = 0
        n = len(s)
        
        while i < n:
            char = s[i]
            if char.isdigit():
                num = num * 10 + int(char)
            if char in "+-*/" or i == n - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack[-1] = stack[-1] * num
                elif sign == "/":
                    stack[-1] = int(stack[-1] / num)  # truncate towards zero
                sign = char
                num = 0
            i += 1
        
        return sum(stack)
