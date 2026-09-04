class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxi = 0
        mini = float('inf')

        for i in range(0,n):
            maxi = max(nums[:i + 1])
            mini = min(nums[i:])
        
            score = maxi - mini
            if score <= k:
                return i
        
        return -1

            