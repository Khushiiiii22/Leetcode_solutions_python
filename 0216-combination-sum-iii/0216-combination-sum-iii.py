class Solution:
    def solve(self,last , total,subset,n , k ,result):
        if total == n and len(subset) == k :
            result.append(subset.copy())
            return
        if total > n or len(subset) > k:
            return
        for i in range(last , 10):
            sum = total + i
            subset.append(i)
            self.solve (i +1,sum , subset,n , k , result )
            subset.pop()
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.solve(1, 0 , [], n , k ,result)
        return result
        