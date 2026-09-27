class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        current = ""

        for ch in s:
            if ch == "(":
                stack.append(current)
                current = ""
            elif ch == ")":
                current = stack.pop() + current[::-1]

            else:
                current += ch 
        return current       