class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows,columns=set(),set()
        boxes={}
        for i in range(3):
            for j in range(3):
                boxes[(i,j)]=set()
        

        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    row,col=i//3,j//3
                    if board[i][j] in rows or board[i][j] in boxes[(row,col)]:
                        return False
                    rows.add(board[i][j])
                    boxes[(row,col)].add(board[i][j])
                if board[j][i]!='.':
                    if board[j][i] in columns:
                        return False
                    columns.add(board[j][i])
            rows.clear()
            columns.clear()
        
        return True
