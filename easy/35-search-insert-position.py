
# https://leetcode.com/problems/search-insert-position/
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) >> 1

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left



    def searchInsert2(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        elif target < nums[0]:
            return 0
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif target > nums[i] and target < nums[i + 1]:
                return i + 1


if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 11
    # nums = [1,3,5,6]
    # target = 7
    solution = Solution()
    m = solution.searchInsert(nums, target)
    print(m)