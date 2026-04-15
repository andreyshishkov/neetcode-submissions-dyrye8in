class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthese_pairs = {
            ')': '(', 
            '}': '{',
            ']': '['
            }
        for parenthes in s:
            if parenthes not in parenthese_pairs:
                stack.append(parenthes)
                continue
            if stack and parenthese_pairs[parenthes] == stack[-1]:
                stack.pop()
            else:
                stack.append(parenthes)
            
        return len(stack) == 0