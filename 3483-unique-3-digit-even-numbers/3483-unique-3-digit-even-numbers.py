class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        from collections import Counter

        freq = Counter(digits)
        count = 0

        for num in range(100, 1000):
            if num % 2 != 0:
                continue

            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            # Check whether we have enough copies
            need = Counter([a, b, c])

            if all(need[d] <= freq[d] for d in need):
                count += 1

        return count
        