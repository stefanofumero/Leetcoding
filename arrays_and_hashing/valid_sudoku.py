"""
You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:
Each row must contain the digits 1-9 without duplicates.
Each column must contain the digits 1-9 without duplicates.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
Return true if the Sudoku board is valid, otherwise return false

Note: A board does not need to be full or be solvable to be valid.


Easy, just don't make confusion with indexes.
"""
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
            First, check every row, every column and every
            sub-grid.
            we know the board is 9x9
        """
        n = 9
        # check rows
        for i in range(9):
            not_repeated = set()
            for j in range(9):
                if board[i][j] != '.':
                    if int(board[i][j]) not in not_repeated:
                        not_repeated.add(int(board[i][j]))
                    else:
                        return False
        # check columns
        for i in range(9):
            not_repeated = set()
            for j in range(9):
                if board[j][i] != '.':
                    if int(board[j][i]) not in not_repeated:
                        not_repeated.add(int(board[j][i]))
                    else:
                        return False
        # check sub-grids
        for i in range(9):
            not_repeated = set()
            r = (i//3)*3
            c = (i%3)*3
            for s in range(r,r+3):
                for t in range(c,c+3):
                    if board[s][t] != '.':
                        if int(board[s][t]) not in not_repeated:
                            not_repeated.add(int(board[s][t]))
                        else:
                            return False


        return True


