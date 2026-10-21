class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True
            previous = float("-inf")

            for start in range(0, n, k):
                chunk = nums[start:start + k]

                # Count descents around the circular chunk.
                drops = [
                    i for i in range(k)
                    if chunk[i] > chunk[(i + 1) % k]
                ]

                if len(drops) > 1:
                    valid = False
                    break

                # Rotate after the descent, if one exists.
                if drops:
                    cut = drops[0] + 1
                    chunk = chunk[cut:] + chunk[:cut]

                if chunk[0] < previous:
                    valid = False
                    break

                previous = chunk[-1]

            if valid:
                ans += k

        return ans
