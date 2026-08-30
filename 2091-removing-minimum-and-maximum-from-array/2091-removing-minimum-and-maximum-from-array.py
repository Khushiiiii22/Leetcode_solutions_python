class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        if min_index > max_index:
            min_index, max_index = max_index, min_index

        # 1. Remove both from the front
        front = max_index + 1

        # 2. Remove both from the back
        back = n - min_index

        # 3. Remove min from front and max from back
        both = (min_index + 1) + (n - max_index)

        return min(front, back, both)
        