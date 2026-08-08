class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        latest = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                latest[j] = i
                j -= 1
            i -= 1

        answer = []
        used_change = False
        j = 0

        for i, ch in enumerate(word1):
            if j == m:
                break

            if ch == word2[j]:
                answer.append(i)
                j += 1

            elif not used_change:
                if j == m - 1 or i < latest[j + 1]:
                    answer.append(i)
                    used_change = True
                    j += 1

        return answer if j == m else []
        