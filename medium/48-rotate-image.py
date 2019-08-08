# 给定一个 n × n 的二维矩阵表示一个图像。
#
# 将图像顺时针旋转 90 度。
#
# 说明：
#
# 你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/rotate-image
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return

        width = len(matrix[0])
        height = len(matrix)

        for h in range(height):
            for w in range(h, width):
                matrix[h][w], matrix[w][h] = matrix[w][h], matrix[h][w]

        for h in range(height):
            matrix[h].reverse()


def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    answer = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]

    # matrix[0][0] = matrix[2][0]
    # matrix[0][1] = matrix[1][0]
    # matrix[0][2] = matrix[0][0]
    #
    # matrix[1][0] = matrix[2][1]
    # matrix[1][1] = matrix[1][1]
    # matrix[1][2] = matrix[0][1]
    #
    # matrix[2][0] = matrix[2][2]
    # matrix[2][1] = matrix[1][2]
    # matrix[2][2] = matrix[0][2]

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    answer = [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4]
    ]

    solution = Solution()
    solution.rotate(matrix)
    assert matrix == answer, matrix


if __name__ == '__main__':
    main()
