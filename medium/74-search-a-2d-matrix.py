# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # 矩阵为空则直接返回
        if not matrix or not matrix[0]:
            return False

        R = len(matrix)
        C = len(matrix[0])

        # 二分查找
        left, right = 0, R * C - 1
        while left < right:

            # 取左中位数
            mid = (left + right) >> 1
            # row = idx // n ， col = idx % n
            mid_val = matrix[mid // C][mid % C]

            # 如果左中间值小于target，那么target一定不在左半区间
            if mid_val < target:
                left = mid + 1
            else:
                right = mid

        # 对最终结果值进行判断
        return matrix[left // C][left % C] == target


class Solution2:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # 矩阵为空则直接返回
        if not matrix or not matrix[0]:
            return False

        R = len(matrix)
        C = len(matrix[0])

        # 如果 target不在矩阵(最小值, 最大值)范围内，直接返回
        if not (matrix[0][0] <= target <= matrix[-1][-1]):
            return False

        r, c = -1, -1

        left, right = 0, R - 1
        while left <= right:

            # 取左中位数
            mid = (left + right) >> 1

            # 如果该行最小值大于 target，那么target不可能在较大的另一半区间内，可能在较小的另一半区间内
            if matrix[mid][0] > target:
                right = mid - 1
            # 如果该行最大值小于 target，那么target不可能在较小的另一半区间内，可能在较大的另一半区间内
            elif matrix[mid][-1] < target:
                left = mid + 1
            # 否则，target可能在当前行内
            else:
                # print(f'{matrix[mid][0]} <= {target} <= {matrix[mid][-1]}')
                r = mid
                break

        left, right = 0, C - 1
        while left < right:

            # 取右中位数
            mid = (left + right) + 1 >> 1

            # 如果右中值大于target，那么target一定不在右半区间
            if matrix[r][mid] > target:
                right = mid - 1
            else:
                left = mid

        c = left

        # 对最终结果值进行判断
        return matrix[r][c] == target


def main():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 22

    solution = Solution()
    result = solution.searchMatrix(matrix, target)
    print(result)


if __name__ == '__main__':
    main()
