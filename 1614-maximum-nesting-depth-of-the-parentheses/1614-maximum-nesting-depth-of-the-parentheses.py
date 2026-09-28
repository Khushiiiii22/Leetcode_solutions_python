class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxi = 0
        for ch in s:
            if ch == "(":
                depth += 1
                maxi = max(maxi,depth)
            elif ch == ")":
                depth -= 1
        return maxi