class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = []
        n = len(candies)
        max = 0 
        for i in range(0,n):
            if candies[i] >= max:
                max = candies[i]

        for i in range(0,n):
            m = candies[i] + extraCandies
            if m >= max:
                result.append(True)
            else:
                result.append(False)
        return result
        
        