# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells
# are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# https://leetcode.com/problems/word-search/

from typing import List


class Solution:

    def __init__(self):
        self._directions = [
            {'row': 0, 'col': -1},
            {'row': 0, 'col': 1},
            {'row': 1, 'col': 0},
            {'row': -1, 'col': 0},
        ]

    def exist(self, board: List[List[str]], word: str) -> bool:

        rows, cols = len(board), len(board[0])

        if rows == 0 or cols == 0:
            return False
        if not word:
            return False
        # if rows * cols < len(word):
        #     return False

        used: List[List[int]] = [[-1 for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    used[row][col] = 0
                    if self._search_letter(board, rows, cols, row, col, word, 1, used):
                        return True
                    used[row][col] = -1

        return False

        # return self._search(board, R, C, )

    def _search_letter(self, board: List[List[str]], rows: int, cols: int,
                       start_row: int, start_col: int, word: str, word_idx: int,
                       used: List[List[int]]):

        # 递归终止的条件
        if word_idx == len(word):
            return board[start_row][start_col] == word[word_idx - 1]

        # 按顺时针从上方开始搜索字符
        for dir in self._directions:

            tmp_row, tmp_col = start_row + dir['row'], start_col + dir['col']

            # 超出索引边界
            if not (0 <= tmp_row <= rows - 1 and 0 <= tmp_col <= cols - 1):
                continue

            # 节点已经使用
            if used[tmp_row][tmp_col] != -1:
                continue

            # 不为对应字符
            if board[tmp_row][tmp_col] != word[word_idx]:
                continue

            used[tmp_row][tmp_col] = word_idx

            if self._search_letter(board, rows, cols, tmp_row, tmp_col, word, word_idx + 1, used):
                return True

        used[start_row][start_col] = -1

        return False


def main():
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'ABCB'
    # board = [
    #     ['Z', 'K', 'Z', 'Z'],
    #     ['A', 'C', 'C', 'E'],
    #     ['K', 'C', 'C', 'Z']
    # ]
    # word = 'ACCCCK'
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "C", "S"],
        ["A", "D", "E", "E"]
    ]
    word = "SEE"
    board = [["a", "a"]]
    word = "aaa"
    solution = Solution()
    result = solution.exist(board, word)
    print(result)


if __name__ == '__main__':
    main()
