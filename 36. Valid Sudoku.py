from typing import List
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = collections.defaultdict(set)
        col_set = collections.defaultdict(set)
        squ_set = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                else:
                    if (board[r][c] in row_set[r] or board[r][c] in col_set[c] or board[r][c] in squ_set[(r // 3, c // 3)]):
                        return False

        
                row_set[r].add(board[r][c])
                col_set[c].add(board[r][c])
                squ_set[(r // 3, c // 3)].add(board[r][c])

        return True