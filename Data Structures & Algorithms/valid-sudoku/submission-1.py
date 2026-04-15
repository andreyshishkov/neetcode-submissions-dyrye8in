class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []

        for i in range(9):
            for j in range(9):
                elem = board[i][j] 
                if elem != '.':
                    res.extend([
                        (elem, i),
                        (j, elem),
                        (elem, i // 3, j // 3)
                    ])

        return len(res) == len(set(res))