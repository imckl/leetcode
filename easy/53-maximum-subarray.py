
# https://leetcode.com/problems/maximum-subarray/
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# 最大子序和 - 动态规划

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_ = nums[0]
        sum_ = nums[0]
        for i in range(1, n):
            sum_ = max(nums[i], sum_ + nums[i])
            max_ = max(sum_, max_)
            # if sum_ > max_:
            #     max_ = sum_
        return max_


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    solution = Solution()
    m = solution.maxSubArray(nums)
    print(m)