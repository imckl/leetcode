# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
# https://leetcode-cn.com/problems/range-sum-query-immutable/

from typing import List


class NumArray(object):

    def __init__(self, nums: List[int]):
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        self._sums = nums

    def sumRange(self, i: int, j: int) -> int:
        return self._sums[j] if i == 0 else self._sums[j] - self._sums[i - 1]


class NumArray3(object):

    def __init__(self, nums: List[int]):
        self._sums = [sum(nums[0:i + 1]) for i in range(len(nums))]

    def sumRange(self, i: int, j: int) -> int:
        return self._sums[j] if i == 0 else self._sums[j] - self._sums[i - 1]


class NumArray2(object):

    def __init__(self, nums: List[int]):
        self._nums = nums

    def sumRange(self, i: int, j: int) -> int:
        return sum(self._nums[i:j + 1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
