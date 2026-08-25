class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        hash_set = set(nums)
        i = 1
        while k*i in hash_set:
            i += 1
        return k*i
        
 
                
        