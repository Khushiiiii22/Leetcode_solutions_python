class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # suffix_min[i] = minimum from i to n-1
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        # prefix maximum while traversing
        maxi = nums[0]

        for i in range(n):
            maxi = max(maxi, nums[i])

            score = maxi - suffix_min[i]

            if score <= k:
                return i

        return -1

        
        