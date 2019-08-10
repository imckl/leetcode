# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

from typing import List


class Solution:

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        width = len(matrix[0])
        for h in range(height):
            for w in range(width):
                if matrix[h][w] == 0:
                    self._mark(matrix, h, w)

        for h in range(height):
            for w in range(width):
                if matrix[h][w] == None:
                    matrix[h][w] = 0

    def _mark(self, matrix: List[List[int]], h: int, w: int) -> None:
        for x in range(len(matrix[h])):
            if matrix[h][x] not in [0, None]:
                matrix[h][x] = None

        for y in range(len(matrix)):
            if matrix[y][w] not in [0, None]:
                matrix[y][w] = None


def main():
    matrix = [
        [0, 1, 2, 0],
        [3, 0, 5, 2],
        [1, 3, 1, 5]
    ]
    solution = Solution()
    result = solution.setZeroes(matrix)
    print(matrix, result)


if __name__ == '__main__':
    main()
