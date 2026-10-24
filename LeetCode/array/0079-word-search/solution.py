class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,columns=len(board),len(board[0])
        movements=[[1,0],[-1,0],[0,1],[0,-1]]
        visited=set()

        def search(row,col,i):
            if i==len(word):
                return True
            for dr,dc in movements:
                r,c=row+dr,col+dc
                if (r in range(rows) and
                c in range(columns) and
                (r,c) not in visited and
                board[r][c]==word[i]):
                    visited.add((r,c))
                    found=search(r,c,i+1)
                    if found:
                        return True
                    visited.remove((r,c))

        for r in range(rows):
            for c in range(columns):
                if board[r][c]==word[0]:
                    visited.clear()
                    visited.add((r,c))
                    res=search(r,c,1)
                    if res:
                        return True

        return False
