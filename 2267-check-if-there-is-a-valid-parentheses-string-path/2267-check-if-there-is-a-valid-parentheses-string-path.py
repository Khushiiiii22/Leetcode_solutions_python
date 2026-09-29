class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # A valid parentheses string must have even length
        if (m + n - 1) % 2 == 1:
            return False

        # dp[i][j] = set of possible balances at (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]

        # Starting cell
        if grid[0][0] == '(':
            dp[0][0].add(1)
        else:
            return False

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                # Get balances from top and left
                previous = set()

                if i > 0:
                    previous |= dp[i - 1][j]

                if j > 0:
                    previous |= dp[i][j - 1]

                # Update balance using current character
                for balance in previous:

                    if grid[i][j] == '(':
                        new_balance = balance + 1
                    else:
                        new_balance = balance - 1

                    # Valid path can never have negative balance
                    if new_balance >= 0:
                        dp[i][j].add(new_balance)

        # At the end, we need balance exactly 0
        return 0 in dp[m - 1][n - 1]
        