class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        factors = [
            (0, 0, 0, 0),  # 0
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        ]

        required = [0, 0, 0, 0]
        value = t

        for prime, index in ((2, 0), (3, 1), (5, 2), (7, 3)):
            while value % prime == 0:
                required[index] += 1
                value //= prime

        if value != 1:
            return "-1"

        need_2 = required[0]
        need_3 = required[1]

        min_two_three = [
            [0] * (need_3 + 1)
            for _ in range(need_2 + 1)
        ]

        for a in range(need_2 + 1):
            for b in range(need_3 + 1):
                best = float("inf")

                for sixes in range(min(a, b) + 1):
                    remaining_2 = a - sixes
                    remaining_3 = b - sixes

                    
                    count = (
                        sixes
                        + (remaining_2 + 2) // 3
                        + (remaining_3 + 1) // 2
                    )

                    best = min(best, count)

                min_two_three[a][b] = best

        def feasible(need, slots):
            a, b, c, d = need

            required_digits = (
                min_two_three[a][b] + c + d
            )

            return required_digits <= slots

        def subtract_digit(need, digit):
            return [
                max(0, need[i] - factors[digit][i])
                for i in range(4)
            ]

        def build_smallest_suffix(need, length):
            result = []

            for position in range(length):
                remaining_slots = length - position - 1

                for digit in range(1, 10):
                    next_need = subtract_digit(need, digit)

                    if feasible(next_need, remaining_slots):
                        result.append(str(digit))
                        need = next_need
                        break

            return "".join(result)

        total = [0, 0, 0, 0]

        for ch in num:
            digit = ord(ch) - ord("0")

            for i in range(4):
                total[i] += factors[digit][i]

        if "0" not in num:
            if all(total[i] >= required[i] for i in range(4)):
                return num

        n = len(num)

        first_zero = num.find("0")
        if first_zero == -1:
            first_zero = n

        prefix_factors = total[:]

        for pivot in range(n - 1, -1, -1):
            old_digit = ord(num[pivot]) - ord("0")

            for i in range(4):
                prefix_factors[i] -= factors[old_digit][i]

 
            if pivot > first_zero:
                continue
            for new_digit in range(old_digit + 1, 10):
                have = prefix_factors[:]

                for i in range(4):
                    have[i] += factors[new_digit][i]

                need = [
                    max(0, required[i] - have[i])
                    for i in range(4)
                ]

                suffix_length = n - pivot - 1

                if feasible(need, suffix_length):
                    return (
                        num[:pivot]
                        + str(new_digit)
                        + build_smallest_suffix(need, suffix_length)
                    )
        minimum_length = (
            min_two_three[required[0]][required[1]]
            + required[2]
            + required[3]
        )

        length = max(n + 1, minimum_length)

        return build_smallest_suffix(required[:], length)