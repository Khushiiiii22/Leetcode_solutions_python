class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        brackets = [""] * (2 * n)
        result = []

        def solve(ind, total, open_count):
            if ind == len(brackets):
                if total == 0:
                    result.append("".join(brackets))
                return

            # Add (
            if open_count < n:
                brackets[ind] = "("
                solve(ind + 1, total + 1, open_count + 1)

            # Add )
            if total > 0:
                brackets[ind] = ")"
                solve(ind + 1, total - 1, open_count)

        solve(0, 0, 0)

        return result