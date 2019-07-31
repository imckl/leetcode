# 给定两个数组，编写一个函数来计算它们的交集。
# https://leetcode-cn.com/problems/intersection-of-two-arrays/

from typing import List


class Solution(object):
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
