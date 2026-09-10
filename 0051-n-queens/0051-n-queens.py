class Solution:
    def solve(self,col,board,ans,lr,ud,ld,n):
        if col == n:
            ans.append(board[:])
            return
        
        for row in range(n):
            if(lr[row]==0 and ld[row+col]==0 and ud[n-1+col-row]==0):
                board[row] = board[row][:col] + "Q" + board[row][col+1:]
                lr[row]=1
                ld[row+col]=1
                ud[n-1+col-row]=1
                self.solve(col+1,board,ans,lr,ud,ld,n)

                board[row] = board[row][:col] + "." + board[row][col+1:]
                lr[row]=0
                ld[row+col]=0
                ud[n-1+col-row]=0


    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = ["." * n for _ in range(n)]
        lr = [0] * n
        ud = [0] *(2*n-1)
        ld = [0] *(2*n-1)
        self.solve(0,board,ans,lr,ud,ld,n)
        return ans
        