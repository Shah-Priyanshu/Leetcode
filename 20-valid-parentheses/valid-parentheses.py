class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # Define a dictionary to map closing brackets to their corresponding opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                # If the current character is a closing bracket
                top_element = stack.pop() if stack else '#'
                # Pop the top element from the stack or use '#' if the stack is empty

                # If the popped element is not the corresponding opening bracket, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # If the current character is an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty at the end, it means all brackets are properly closed
        return not stack