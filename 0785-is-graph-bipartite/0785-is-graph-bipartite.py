class Solution:
    def dfs(self,curr,vis,graph,color):
        vis[curr] = color
        for aN in graph[curr]:
            if vis[aN] != -1:
                if vis[aN] == color:
                    return False
            else:
                ans = self.dfs(aN,vis,graph,1-color)
                if ans == False:
                    return False
        return True

    def isBipartite(self, graph: list[list[int]]) -> bool:
        total = len(graph)
        vis = [-1] * total
        for i in range(0,total):
            if vis[i] == -1:
                ans = self.dfs(i,vis,graph,0)

                if ans == False:
                    return False
        return True
        