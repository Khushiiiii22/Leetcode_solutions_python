class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l = 0
        r = 0
        n = len(g)
        m = len(s)
        g.sort()
        s.sort()
        count= 0
        while l<n and r<m:
            if g[l] <= s[r]:
                count+=1
                l+=1
            r+=1
        return count
        