class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        # Store reserved seats for each row
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        # Every completely empty row can fit 2 groups
        ans = 2 * n

        for row in rows:
            reserved = rows[row]

            left = 2 not in reserved and 3 not in reserved and \
                   4 not in reserved and 5 not in reserved

            middle = 4 not in reserved and 5 not in reserved and \
                     6 not in reserved and 7 not in reserved

            right = 6 not in reserved and 7 not in reserved and \
                    8 not in reserved and 9 not in reserved

            if left and right:
                # Already counted 2 for this row
                continue

            elif left or middle or right:
                # This row can only fit 1 group
                ans -= 1

            else:
                # This row cannot fit any group
                ans -= 2

        return ans
        