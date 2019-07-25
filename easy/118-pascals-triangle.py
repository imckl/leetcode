
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
# https://leetcode.com/problems/pascals-triangle/

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        pascals_triangle = [[1], [1, 1]]
        for i in range(2, numRows):
            bottom = [1]
            for j in range(len(pascals_triangle[-1]) - 1):
                bottom.append(pascals_triangle[-1][j] + pascals_triangle[-1][j + 1])
            bottom.append(1)
            pascals_triangle.append(bottom)
        return pascals_triangle


if __name__ == '__main__':
    numRows = 10
    s = Solution()
    print(s.generate(numRows))
