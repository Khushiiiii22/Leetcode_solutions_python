from bisect import bisect_right
from typing import List
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Add original index
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        # Sort by starting position
        arr.sort()

        n = len(arr)

        # Starting positions for binary search
        starts = [x[0] for x in arr]

        # next_idx[i] = first interval whose start > arr[i].right
        next_idx = [0] * n

        for i in range(n):
            next_idx[i] = bisect_right(starts, arr[i][1])

        # dp[k][i] = (maximum score, lexicographically smallest indices)
        #
        # We process from right to left.
        dp = [[(0, ()) for _ in range(n + 1)] for _ in range(5)]

        for k in range(1, 5):

            for i in range(n - 1, -1, -1):

                # Option 1: don't take this interval
                skip_score, skip_indices = dp[k][i + 1]

                # Option 2: take this interval
                l, r, weight, original_index = arr[i]

                next_i = next_idx[i]

                take_score = weight + dp[k - 1][next_i][0]

                take_indices = tuple(
                    sorted(
                        (original_index,) + dp[k - 1][next_i][1]
                    )
                )

                # Choose the better option
                if take_score > skip_score:
                    dp[k][i] = (take_score, take_indices)

                elif take_score < skip_score:
                    dp[k][i] = (skip_score, skip_indices)

                else:
                    # Same score → lexicographically smaller indices
                    dp[k][i] = min(
                        (take_score, take_indices),
                        (skip_score, skip_indices)
                    )

        return list(dp[4][0][1])
        