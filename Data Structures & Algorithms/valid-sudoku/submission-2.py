class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        records = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row = (board[i][j], i)
                    col = (j, board[i][j])
                    sq = (board[i][j], i // 3, j // 3)
                    if row in records or col in records or sq in records:
                        return False
                    records.add(row)
                    records.add(col)
                    records.add(sq)
        return True