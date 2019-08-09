# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
# https://leetcode-cn.com/problems/spiral-matrix/

from typing import List


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        result = []

        def move_to_rightmost():
            """移动至矩阵第一行最右端，移动时输出当前值至结果列表"""

            # 矩阵为空，直接返回
            if not matrix:
                return

            # 输出矩阵第一行最左端（栈尾）值出栈至结果列表，直至栈为空
            while matrix[0]:
                result.append(matrix[0].pop(0))
            # 从矩阵中移除首行空栈
            matrix.pop(0)

        def move_to_bottom():
            """移动到最底部，并将每行最右端值输出至结果列表"""

            # 矩阵为空，直接返回
            if not matrix:
                return

            # 顺序输出矩阵每行的最右端值至结果列表
            for row in matrix:
                if not row:
                    continue
                # 输出栈顶（最右端）值至结果列表
                result.append(row.pop())

        def move_to_leftmost():
            """移动至矩阵最后一行最左端，移动时输出当前值至结果列表"""

            # 矩阵为空，直接返回
            if not matrix:
                return

            # 输出矩阵最后一行最右端（栈顶）值出栈至结果列表，直至栈为空
            while matrix[-1]:
                result.append(matrix[-1].pop())
            # 从矩阵中移除尾行空栈
            matrix.pop(-1)

        def move_to_top():
            """移动到最顶部，并将每行最左端值输出至结果列表"""

            # 矩阵为空，直接返回
            if not matrix:
                return

            # 输出矩阵每行的最左端值至结果列表
            for row in matrix[::-1]:
                if not row:
                    continue
                # 输出栈尾（最左端）值至结果列表
                result.append(row.pop(0))

        # 按题设要求顺序执行，直至矩阵为空（所有值都出栈）
        while matrix:
            move_to_rightmost()
            # print('r', result, matrix)
            move_to_bottom()
            # print('b', result, matrix)
            move_to_leftmost()
            # print('l', result, matrix)
            move_to_top()
            # print('t', result, matrix)

        return result


def main():
    # matrix = [
    #     [1, 2, 3, 4],
    #     [5, 6, 7, 8],
    #     [9, 10, 11, 12],
    #     [13, 14, 15, 16]
    # ]
    # answer = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 11, 7, 5, 6, 10, 9]
    # solution = Solution()
    # result = solution.spiralOrder(matrix)

    matrix_list = [
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ],
        [
            [7],
            [9],
            [6]
        ],
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
    ]
    answer_list = [
        [1, 2, 3, 6, 9, 8, 7, 4, 5],
        [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        [7, 9, 6],
        [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    ]

    for matrix, answer in zip(matrix_list, answer_list):
        solution = Solution()
        result = solution.spiralOrder(matrix)
        assert result == answer, f'output: {result}, expect: {answer}'


if __name__ == '__main__':
    main()
