# https://leetcode-cn.com/problems/valid-sudoku/

from typing import List
from collections import Counter


class SolutionNotMine:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 记录所有出现的行、列、块中的所有字符出现的位置
        # 格式为(行，数字),(数字，列),(行，列，数字)
        ret = []
        for i, row in enumerate(board):
            for j, digit in enumerate(row):
                if digit != '.':
                    ret += [(digit, i), (j, digit), (i // 3, j // 3, digit)]
        print(ret)
        return len(ret) == len(set(ret))


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_count = len(board)
        column_count = len(board[0])

        # 构造并检查行
        for row in board:
            if not self._valid_list([cell for cell in row if cell != '.']):
                return False

        # 构造并检查列
        for column in range(column_count):
            if not self._valid_list([row[column] for row in board if row[column] != '.']):
                return False

        # 构造并检查子九宫格
        for i in range(0, column_count, 3):
            for j in range(0, row_count, 3):
                if not self._valid_list(
                        [board[k][l] for l in range(j, j + 2 + 1) for k in range(i, i + 2 + 1) if board[k][l] != '.' ]):
                    return False

        return True

    def _valid_list(self, list_: List[str]) -> bool:
        # 使用集合去重，如果集合元素个数与数组元素个数相等，则说明无重复
        return len(list_) == len(set(list_))



class Solution2:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_count = len(board)
        column_count = len(board[0])

        # valid rows
        # consrtuct row
        for row in board:
            if not self._valid_list(row):
                return False

        # valid columns
        # construct column
        for column in range(column_count):
            if not self._valid_list([row[column] for row in board]):
                return False

        # valid squares
        # construct square
        for i in range(0, column_count, 3):
            for j in range(0, row_count, 3):
                if not self._valid_list([board[k][l] for l in range(j, j + 2 + 1) for k in range(i, i + 2 + 1)]):
                    return False

        return True

    def _valid_list(self, row: List[str]) -> bool:
        row = [c for c in row if c != '.']
        return Counter(row).most_common(1)[0][1] == 1 if row else True

