class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence of every character
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Find the smallest valid interval starting from each character
        for ch in range(26):
            if last[ch] == -1:
                continue

            left = first[ch]
            right = last[ch]
            valid = True

            i = left

            while i <= right:
                idx = ord(s[i]) - ord('a')

                # This character appeared before our left boundary
                if first[idx] < left:
                    valid = False
                    break

                # This character has another occurrence farther right
                right = max(right, last[idx])

                i += 1

            if valid:
                intervals.append((right, left))

        # Choose non-overlapping intervals that finish earliest
        intervals.sort()

        result = []
        prev_end = -1

        for right, left in intervals:
            if left > prev_end:
                result.append(s[left:right + 1])
                prev_end = right

        return result
        