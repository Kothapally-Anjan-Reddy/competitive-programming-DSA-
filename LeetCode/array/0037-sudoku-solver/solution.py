class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows,columns=[set() for _ in range(9)],[set() for _ in range(9)]
        boxes={}    #It has all small 9 box
        for i in range(3):
            for j in range(3):
                boxes[(i,j)]=set()
        tobedone=[]

        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    tobedone.append((i,j))
                else:
                    rows[i].add(board[i][j])
                    columns[j].add(board[i][j])
                    boxes[(i//3,j//3)].add(board[i][j])
        
        
        def solve(idx):
            if idx>=len(tobedone):
                return True
            i,j=tobedone[idx]
            
            for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if num not in rows[i] and num not in columns[j] and num not in boxes[(i//3,j//3)]:
                    board[i][j]=num
                    rows[i].add(num)
                    columns[j].add(num)
                    boxes[(i//3,j//3)].add(num)
                    
                    if solve(idx+1):
                        return True

                    board[i][j]='.'
                    rows[i].remove(num)
                    columns[j].remove(num)
                    boxes[(i//3,j//3)].remove(num)

        solve(0)
