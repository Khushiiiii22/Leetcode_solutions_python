class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower(nums,target):
            n = len(nums)
            lb = n
            low = 0 
            high = n-1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= target:
                    lb = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return lb
        def upper(nums , target):
            n = len(nums)
            ub = n
            low = 0 
            high = n-1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] > target:
                    ub = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return ub
        lb = lower(nums,target)
        if lb == len(nums) or nums[lb] != target:
            return[-1,-1]
        ub = upper(nums,target)
        return(lb,ub-1)

                    
        