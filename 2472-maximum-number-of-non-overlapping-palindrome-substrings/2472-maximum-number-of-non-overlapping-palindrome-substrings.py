class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # dp[i][j] = True if s[i:j+1] is a palindrome
        dp = [[False] * n for _ in range(n)]

        # Store all valid palindrome intervals
        intervals = []

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and (length <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True

                    if length >= k:
                        intervals.append((i, j))

        # Greedy: choose interval that finishes earliest
        intervals.sort(key=lambda x: x[1])

        count = 0
        last_end = -1

        for start, end in intervals:
            if start > last_end:
                count += 1
                last_end = end

        return count
        