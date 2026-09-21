class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        current = [0] * k

        for num in nums:
            new = [0] * k

            # Start a new subarray with just num
            remainder = num % k
            new[remainder] += 1

            # Extend previous subarrays
            for r in range(k):
                new[(r * num) % k] += current[r]

            current = new

            # Add all subarrays ending here to the answer
            for r in range(k):
                result[r] += current[r]

        return result
        