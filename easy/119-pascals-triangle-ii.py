
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# https://leetcode-cn.com/problems/pascals-triangle-ii/

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            row = [m + n for m, n in zip([0] + row, row + [0])]
        return row

    def getRow2(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        bottom = [1, 1]
        cur_index = 2
        while cur_index <= rowIndex:
            cur_bottom = [1]
            for i in range(len(bottom) - 1):
                cur_bottom.append(bottom[i] + bottom[i + 1])
            cur_bottom.append(1)
            bottom = cur_bottom
            cur_index += 1
        return bottom

    def getRow3(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        return self._get_row(rowIndex + 1 - 2, [1, 1])

    def _get_row(self, remainDepth: int, bottom: List[int]) -> List[int]:
        if remainDepth == 0:
            return bottom
        new_bottom = [1]
        for i in range(len(bottom) - 1):
            new_bottom.append(bottom[i] + bottom[i + 1])
        new_bottom.append(1)
        return self._get_row(remainDepth - 1, new_bottom)


if __name__ == '__main__':
    rowIndex = 100
    s = Solution()
    print(s.getRow(rowIndex))
