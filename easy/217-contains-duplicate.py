# 给定一个整数数组，判断是否存在重复元素。
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

from typing import List


class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
