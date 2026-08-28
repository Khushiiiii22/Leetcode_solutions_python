class Solution:
    def backtrack(self,index,total,subset,nums,target,result):
        if total == 0 :
            result.append(subset.copy())
            return
        if total < 0:
            return
        if index >= len(nums):
            return
        for i in range(index,len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            sum = total - nums[i]
            self.backtrack(i+1,sum,subset,nums,target,result)
            subset.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.backtrack(0,target,[],candidates,target,result)
        return result

        