class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)

        seen = set()
        duplicate = -1

        for x in nums:
            if x in seen:
                duplicate = x
            seen.add(x)
        
        total = n * (n + 1) // 2
        actual = sum(nums)

        missing = total - (actual-duplicate)
        return [duplicate,missing]
        

        