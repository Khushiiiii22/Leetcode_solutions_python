class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def parse(i):
            # This stores all possible words for the
            # expression we are currently parsing.
            result = set()

            # current represents the concatenation
            # built so far.
            current = {""}

            while i < len(expression) and expression[i] != "}":

                # Comma means:
                # finish the current expression and
                # take UNION with the next expression.
                if expression[i] == ",":
                    result.update(current)
                    current = {""}
                    i += 1

                # Opening brace means:
                # recursively parse everything inside it.
                elif expression[i] == "{":
                    next_set, i = parse(i + 1)

                    # Concatenate current × next_set
                    current = {
                        a + b
                        for a in current
                        for b in next_set
                    }

                # Otherwise it is a lowercase letter.
                else:
                    ch = expression[i]

                    current = {
                        word + ch
                        for word in current
                    }

                    i += 1

            # Add whatever was built after the last comma.
            result.update(current)

            # If we stopped because of }, skip it.
            if i < len(expression) and expression[i] == "}":
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)
        
        