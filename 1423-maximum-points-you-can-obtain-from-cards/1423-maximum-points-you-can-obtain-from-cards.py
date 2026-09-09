class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
        l_s = 0
        r_s = 0

        for i in range(0,k):
            l_s += cardPoints[i]
        maxi = l_s
        r_i = n-1

        for i in range(k-1,-1,-1):
            l_s -= cardPoints[i]
            r_s += cardPoints[r_i]
            maxi = max(maxi,l_s+r_s)
            r_i -= 1
        return maxi
        