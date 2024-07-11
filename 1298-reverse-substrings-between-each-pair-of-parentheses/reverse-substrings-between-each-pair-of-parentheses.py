class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # Pop characters until the corresponding '(' is found
                substring = []
                while stack and stack[-1] != '(':
                    substring.append(stack.pop())
                # Remove the '(' from the stack
                stack.pop()
                # Reverse the substring and add it back to the stack
                stack.extend(substring)
            else:
                stack.append(char)
        
        # Join the stack to form the final result string
        return ''.join(stack)
