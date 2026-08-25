class Solution:
    def isValid(self, s: str) -> bool:
        matching = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c in matching and matching[c] and stack and matching[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
            
        return not stack