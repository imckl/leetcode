
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
# 说明:
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。
# https://leetcode-cn.com/problems/rotate-array/

todo

from typing import List


class Solution(object):
    class Solution:
        def rotate(self, nums: List[int], k: int) -> None:
            nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]



class Solution2(object):
    class Solution:
        def rotate(self, nums: List[int], k: int) -> None:
            nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
