class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        n = len(target)
        prefix = []

        for i in range(n):
            t = ord(target[i]) - ord('a')

            # We cannot continue matching target here
            if freq[t] == 0:
                # First, try to make this position slightly bigger
                for c in range(t + 1, 26):
                    if freq[c] > 0:
                        freq[c] -= 1

                        ans = ''.join(prefix)
                        ans += chr(c + ord('a'))

                        # Remaining characters in sorted order
                        for x in range(26):
                            ans += chr(x + ord('a')) * freq[x]

                        return ans

                break

            # Match target[i]
            freq[t] -= 1
            prefix.append(target[i])

        # We matched the entire target exactly.
        # Now we must backtrack and make some position bigger.
        for i in range(len(prefix) - 1, -1, -1):
            idx = ord(prefix[i]) - ord('a')

            # Return the character at this position
            freq[idx] += 1

            # Find the smallest character greater than it
            for c in range(idx + 1, 26):
                if freq[c] > 0:
                    freq[c] -= 1

                    ans = ''.join(prefix[:i])
                    ans += chr(c + ord('a'))

                    for x in range(26):
                        ans += chr(x + ord('a')) * freq[x]

                    return ans

        return ""