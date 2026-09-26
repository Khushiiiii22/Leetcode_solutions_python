class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        values = {}

        # Store key -> value
        for key, value in knowledge:
            values[key] = value

        result = []
        i = 0

        while i < len(s):

            # Start of a bracket pair
            if s[i] == '(':
                j = i + 1

                # Find closing bracket
                while s[j] != ')':
                    j += 1

                # Extract key
                key = s[i + 1:j]

                # Look up key
                if key in values:
                    result.append(values[key])
                else:
                    result.append("?")

                # Move past ')'
                i = j + 1

            else:
                # Normal character
                result.append(s[i])
                i += 1

        return "".join(result)
        