class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))

    def pop(self):
        # Pop the top elements - both stacks
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        # Return the top element - main stack
        return self.stack[-1]

    def getMin(self):
        # Return the top element - min_stack
        return self.min_stack[-1]
