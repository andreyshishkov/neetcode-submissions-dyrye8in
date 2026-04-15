class Solution:
    def isValid(self, s: str) -> bool:
        closed = ']})'
        pairs = {']': '[', '}': '{', ')': '('}
        stack = []

        for symb in s:
            if symb in closed and stack and pairs[symb] == stack[-1]:
                stack.pop()
                continue
            stack.append(symb)

        return len(stack) == 0
