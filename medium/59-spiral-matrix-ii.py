# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
# https://leetcode-cn.com/problems/spiral-matrix-ii/

from typing import List


class Solution:

    def generateMatrix(self, n: int) -> List[List[int]]:

        # 预创建矩阵
        matrix = [[0] * n for _ in range(n)]

        # 当前数值
        i = 1

        # 从最外层向最内层，逐层构造
        # 内层比外层少2个元素
        for j in range(n, 0, -2):

            # 当前层数的起始x, y
            start_x, start_y = (n - j) // 2, (n - j) // 2

            # 本次遍历起始的x, y
            x, y = 0, 0

            # 开始遍历，每层至多遍历4 * (j - 1)次
            for k in range(4 * (j - 1)):

                # 设置矩阵对应位置的值
                # 当前层的起始坐标加上遍历过程中变化的坐标，即是整个矩阵中对应的位置
                matrix[start_y + y][start_x + x] = i
                # 数值加一
                i += 1

                # 顺序填充，第一行
                if 0 <= k < j - 1:
                    # 顺序增一
                    x += 1
                # 顺序谭崇，最后一列
                elif j - 1 <= k < 2 * (j - 1):
                    # 顺序增一
                    y += 1
                # 逆序填充，最后一行
                elif 2 * (j - 1) <= k < 3 * (j - 1):
                    # 逆序增一
                    x -= 1
                # 逆序填充，第一列
                elif 3 * (j - 1) <= k < 4 * (j - 1):
                    # 逆序增一
                    y -= 1

        # 如果n为奇数，则最中间的的数仍未调整
        if n % 2:
            matrix[n // 2][n // 2] = i

        return matrix


def main():
    n = 10
    solution = Solution()
    result = solution.generateMatrix(n)
    for _ in result:
        print(_)


if __name__ == '__main__':
    main()
