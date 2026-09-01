from collections import deque
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        start = None
        litter_id = {}
        cnt = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = cnt
                    cnt += 1

        if cnt == 0:
            return 0

        full_mask = (1 << cnt) - 1

        # State: (row, col, mask, energy)
        q = deque([(start[0], start[1], 0, energy, 0)])

        # best[(r,c,mask)] = maximum energy we've had there
        best = {(start[0], start[1], 0): energy}

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, mask, e, dist = q.popleft()

            if e == 0:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                ne = e - 1
                nmask = mask

                # Collect litter
                if classroom[nr][nc] == 'L':
                    nmask |= 1 << litter_id[(nr, nc)]

                # Reset energy
                if classroom[nr][nc] == 'R':
                    ne = energy

                nd = dist + 1

                if nmask == full_mask:
                    return nd

                key = (nr, nc, nmask)

                # If we've already reached this state with
                # at least as much energy, this state is useless.
                if best.get(key, -1) >= ne:
                    continue

                best[key] = ne
                q.append((nr, nc, nmask, ne, nd))

        return -1
        