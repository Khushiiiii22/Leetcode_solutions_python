class Solution:
    def reverseDegree(self, s: str) -> int:
        answer = 0

        for i, ch in enumerate(s):
            position = i + 1
            reverse_value = 26 - (ord(ch) - ord('a'))
            answer += reverse_value * position

        return answer
        