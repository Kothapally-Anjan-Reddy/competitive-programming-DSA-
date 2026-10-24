class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[['.']*n for i in range(n)]
        result=[]
        col=set()
        pos=set()
        neg=set()
        
        def dfs(i):
            if i>=n:
                res=["".join(x) for x in board]
                result.append(res)
                return
            
            for j in range(n):
                if j not in col and (i-j) not in neg and (i+j) not in pos:
                    col.add(j)
                    pos.add(i+j)
                    neg.add(i-j)
                    board[i][j]='Q'
                    dfs(i+1)
                    col.remove(j)
                    pos.remove(i+j)
                    neg.remove(i-j)
                    board[i][j]='.'
        dfs(0)
        return result
