class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        max_l = 0
        l = 0
        r = 0 
        dicti = {}
        while r < n:
            dicti[fruits[r]] = dicti.get(fruits[r],0) + 1
            if len(dicti) > 2:
                dicti[fruits[l]] -= 1
                if dicti[fruits[l]] == 0:
                    del dicti[fruits[l]]
                l += 1
            if len(dicti) <= 2:
                max_l = max(max_l,r-l+1)
            r += 1
        return max_l
        