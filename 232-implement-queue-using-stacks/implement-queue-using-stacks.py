class MyQueue:
    def __init__(self):
        self.stack_push = []
        self.stack_pop = []

    def push(self, x: int) -> None:
        self.stack_push.append(x)

    def pop(self) -> int:
        self._transfer()
        return self.stack_pop.pop()

    def peek(self) -> int:
        self._transfer()
        return self.stack_pop[-1]

    def empty(self) -> bool:
        return len(self.stack_push) == 0 and len(self.stack_pop) == 0

    def _transfer(self) -> None:
        if not self.stack_pop:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())