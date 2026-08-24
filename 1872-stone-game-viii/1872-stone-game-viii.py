class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)

        # prefix[i] = sum of first i stones
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        dp = [0] * (n + 1)

        # State n = only one stone remains
        dp[n] = 0

        # best = max(prefix[j] - dp[j]) for j > i
        best = prefix[n]

        for i in range(n - 1, 0, -1):
            dp[i] = best

            # For i >= 2, this state can be used by the initial move.
            if i >= 2:
                best = max(best, prefix[i] - dp[i])

        # Alice's first move must take at least 2 stones
        dp[0] = best

        return dp[0]
        