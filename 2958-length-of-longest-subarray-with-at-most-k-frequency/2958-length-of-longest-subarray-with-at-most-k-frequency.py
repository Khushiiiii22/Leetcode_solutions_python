class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency = defaultdict(int)
        left = 0
        answer = 0

        for right, value in enumerate(nums):
            frequency[value] += 1
            while frequency[value] > k:
                frequency[nums[left]] -= 1
                left += 1

            answer = max(answer, right - left + 1)

        return answer

        