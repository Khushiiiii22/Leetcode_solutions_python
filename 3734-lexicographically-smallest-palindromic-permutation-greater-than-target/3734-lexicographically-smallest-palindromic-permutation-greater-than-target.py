class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        from collections import Counter

        n = len(s)
        half_len = n // 2

        freq = Counter(s)

        # Check if a palindrome is possible
        odd = 0
        middle = ""

        for ch in freq:
            if freq[ch] % 2 == 1:
                odd += 1
                middle = ch

        if odd > 1:
            return ""

        # Characters available for the left half
        half_count = [0] * 26

        for ch in freq:
            half_count[ord(ch) - ord('a')] = freq[ch] // 2

        target_half = target[:half_len]

        # Build palindrome from a given left half
        def make_palindrome(left):
            if n % 2 == 1:
                return left + middle + left[::-1]
            return left + left[::-1]

        # ------------------------------------------------
        # STEP 1: Try to use target's first half exactly
        # ------------------------------------------------

        remaining = half_count[:]
        possible = True

        for ch in target_half:
            idx = ord(ch) - ord('a')

            if remaining[idx] == 0:
                possible = False
                break

            remaining[idx] -= 1

        if possible:
            candidate = make_palindrome(target_half)

            # It has the same first half as target,
            # so compare the complete palindrome.
            if candidate > target:
                return candidate

        # ------------------------------------------------
        # STEP 2: Find smallest half > target_half
        # ------------------------------------------------

        remaining = half_count[:]
        prefix = []

        for i in range(half_len):

            idx = ord(target_half[i]) - ord('a')

            # Match target[i] if possible
            if remaining[idx] > 0:
                remaining[idx] -= 1
                prefix.append(target_half[i])
                continue

            # Can't match target[i].
            # Try the smallest character greater than it.
            for c in range(idx + 1, 26):
                if remaining[c] > 0:
                    remaining[c] -= 1

                    left = ''.join(prefix) + chr(c + ord('a'))

                    # Put remaining characters in sorted order
                    for x in range(26):
                        left += chr(x + ord('a')) * remaining[x]

                    return make_palindrome(left)

            break

        # ------------------------------------------------
        # STEP 3: We matched the whole target half.
        # Backtrack and increase the rightmost possible position.
        # ------------------------------------------------

        for i in range(len(prefix) - 1, -1, -1):

            idx = ord(prefix[i]) - ord('a')

            # Put this character back
            remaining[idx] += 1

            # Find smallest character > target[i]
            for c in range(idx + 1, 26):
                if remaining[c] > 0:
                    remaining[c] -= 1

                    left = ''.join(prefix[:i])
                    left += chr(c + ord('a'))

                    # Remaining characters sorted
                    for x in range(26):
                        left += chr(x + ord('a')) * remaining[x]

                    return make_palindrome(left)

        return ""