class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_count = 0

        i = 0
        while i < len(s):
            if s[i] == '(':
                open_count += 1

            else:
                # Check whether this is the first ')' of a pair
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1  # Consume the second ')'
                else:
                    insertions += 1  # Insert a missing ')'

                if open_count > 0:
                    open_count -= 1
                else:
                    insertions += 1  # Insert a missing '('

            i += 1

        # Every remaining '(' needs two closing ')'
        insertions += open_count * 2

        return insertions
        