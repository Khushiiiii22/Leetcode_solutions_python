class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x, reverse=True)

        n = len(nums)
        score = 0

        for i, num in enumerate(nums):
            if i < (n + 1) // 2:
                score += num * num
            else:
                score -= num * num

        return score
        