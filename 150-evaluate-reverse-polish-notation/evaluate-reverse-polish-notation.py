class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # Stack to keep track of numbers
        stack = []
        
        # Iterate through each token
        for token in tokens:
            # If token is an operator, apply it to the last two numbers in the stack
            if token in ["+", "-", "*", "/"]:
                num2 = stack.pop()
                num1 = stack.pop()
                
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    # Perform integer division with truncation towards zero
                    stack.append(int(float(num1) / num2))
            else:
                # Token is a number, push it onto the stack
                stack.append(int(token))
                
        # The final answer is the last number in the stack
        return stack.pop()