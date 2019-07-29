# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。
# 说明:
# 你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
# https://leetcode-cn.com/problems/missing-number/

from typing import List


class Solution(object):
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        # 高斯公式
        expected_sum = length * (length + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


class Solution4(object):
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ nums[i]
        return missing


class Solution3(object):
    def missingNumber(self, nums: List[int]) -> int:
        return sum([i for i in range(len(nums) + 1)]) - sum(nums)


class Solution2(object):
    def missingNumber(self, nums: List[int]) -> int:
        for num in range(len(nums) + 1):
            if num not in nums:
                return num
