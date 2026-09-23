class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)

        # We want to keep the longest subarray
        # whose sum is total - x
        target = total - x

        if target < 0:
            return -1

        left = 0
        curr_sum = 0
        max_len = -1

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum > target and left <= right:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == target:
                max_len = max(max_len, right - left + 1)

        if max_len == -1:
            return -1

        return len(nums) - max_len
        