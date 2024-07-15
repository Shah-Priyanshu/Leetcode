class Solution:
    def calculate(self, s: str) -> int:
        def update_result_and_reset():
            nonlocal result, current_number, sign
            result += sign * current_number
            current_number = 0
            sign = 1

        stack = []
        current_number = 0
        result = 0
        sign = 1  # 1 means positive, -1 means negative

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char in '+-':
                update_result_and_reset()
                sign = 1 if char == '+' else -1
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                update_result_and_reset()
                result *= stack.pop()  # sign before the parenthesis
                result += stack.pop()  # result before the parenthesis
            elif char == ' ':
                continue
        
        result += sign * current_number
        return result
