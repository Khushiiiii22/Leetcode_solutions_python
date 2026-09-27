class Solution:
    def dfs(self,i,j,visited,grid):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        if grid[i][j] == "0":
            return
        if visited[i][j] == 1:
            return
        visited[i][j] = 1

        self.dfs(i+1,j,visited,grid)
        self.dfs(i-1,j,visited,grid)
        self.dfs(i,j+1,visited,grid)
        self.dfs(i,j-1,visited,grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        count = 0
        visited = [[0 for _ in range(c)]for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    count += 1
                    self.dfs(i,j,visited,grid)
        return count
        