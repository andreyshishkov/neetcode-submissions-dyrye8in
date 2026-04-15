class MinStack:

    def __init__(self):
        self._values_stack = []
        self._min_stack = []
        

    def push(self, val: int) -> None:
        if not self._values_stack:
            self._values_stack.append(val)
            self._min_stack.append(val)
            return
        self._values_stack.append(val)
        self._min_stack.append(min(val, self._min_stack[-1]))

    def pop(self) -> None:
        self._min_stack.pop()
        self._values_stack.pop()
        

    def top(self) -> int:
        return self._values_stack[-1]
        

    def getMin(self) -> int:
        return self._min_stack[-1]
        
