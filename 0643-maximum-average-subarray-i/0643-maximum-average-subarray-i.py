class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        left = 0
        right = k-1
        curr = sum(nums[left:right+1])
        maxi = curr
        while right<n-1:
            right+=1
            curr = curr - nums[left] + nums[right]
            maxi = max(maxi,curr)
            left+= 1
        return maxi/k
        
        