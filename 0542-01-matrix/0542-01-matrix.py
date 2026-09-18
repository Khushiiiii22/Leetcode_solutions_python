class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        r = len(mat)
        c = len(mat[0])
        visited = [[0 for _ in range(c)] for _ in range(r)]
        distance = [[0 for _ in range(c)] for _ in range(r)]
        queue = deque()
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    queue.append([i,j,0])
                    visited[i][j] = 1
        while len(queue) != 0:
            p,q,d = queue.popleft()
            distance[p][q] = d
            for x , y in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_p , new_q = p+x, q+y 
                if new_p < 0 or new_p >= r or new_q < 0 or new_q >= c:
                    continue
                if visited[new_p][new_q] == 1:
                    continue 
                visited[new_p][new_q] = 1
                queue.append([new_p,new_q,d+1])
        return distance     