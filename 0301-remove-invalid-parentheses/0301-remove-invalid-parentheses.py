class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == "(":
                left_remove += 1

            elif ch == ")":
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        def backtrack(index, current, balance, left_remove, right_remove):

            # Invalid: too many ')'
            if balance < 0:
                return

            if index == len(s):

                if balance == 0 and left_remove == 0 and right_remove == 0:
                    result.add("".join(current))

                return

            ch = s[index]

            # Option 1: remove this parenthesis
            if ch == "(" and left_remove > 0:
                backtrack(
                    index + 1,
                    current,
                    balance,
                    left_remove - 1,
                    right_remove
                )

            elif ch == ")" and right_remove > 0:
                backtrack(
                    index + 1,
                    current,
                    balance,
                    left_remove,
                    right_remove - 1
                )

            # Option 2: keep this character
            if ch == "(":
                current.append(ch)

                backtrack(
                    index + 1,
                    current,
                    balance + 1,
                    left_remove,
                    right_remove
                )

                current.pop()

            elif ch == ")":
                current.append(ch)

                backtrack(
                    index + 1,
                    current,
                    balance - 1,
                    left_remove,
                    right_remove
                )

                current.pop()

            else:
                # Letter → always keep
                current.append(ch)

                backtrack(
                    index + 1,
                    current,
                    balance,
                    left_remove,
                    right_remove
                )

                current.pop()

        backtrack(0, [], 0, left_remove, right_remove)

        return list(result)
        