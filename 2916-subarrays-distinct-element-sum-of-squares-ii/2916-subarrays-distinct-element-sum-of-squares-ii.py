class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        total = [0] * (4 * n)
        squares = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def update(node, start, end, left, right):
            if left <= start and end <= right:
                length = end - start + 1

                squares[node] = (
                    squares[node] + 2 * total[node] + length
                ) % MOD

                total[node] = (total[node] + length) % MOD
                lazy[node] += 1
                return

            mid = (start + end) // 2

            if lazy[node]:
                val = lazy[node]

                for child, a, b in (
                    (node * 2, start, mid),
                    (node * 2 + 1, mid + 1, end)
                ):
                    length = b - a + 1
                    squares[child] = (
                        squares[child]
                        + 2 * val * total[child]
                        + val * val * length
                    ) % MOD
                    total[child] = (
                        total[child] + val * length
                    ) % MOD
                    lazy[child] += val

                lazy[node] = 0

            if left <= mid:
                update(node * 2, start, mid, left, right)

            if right > mid:
                update(node * 2 + 1, mid + 1, end, left, right)

            total[node] = (
                total[node * 2] + total[node * 2 + 1]
            ) % MOD

            squares[node] = (
                squares[node * 2] + squares[node * 2 + 1]
            ) % MOD

        last_seen = {}
        answer = 0

        for i, num in enumerate(nums):
            prev = last_seen.get(num, -1)

            update(1, 0, n - 1, prev + 1, i)

            answer = (answer + squares[1]) % MOD
            last_seen[num] = i

        return answer
        