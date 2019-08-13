# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and
# return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place
# with O(1) extra memory.

from typing import List


class Solution:

    def removeDuplicates(self, nums: List[int]) -> int:

        # 数组为空，返回0
        if not nums:
            return 0

        # 预设第一个字符
        i = 0
        count = 1
        char = nums[0]

        # Python do..while
        while True:

            i += 1

            if i > len(nums) - 1:
                break

            if nums[i] == char:
                count += 1
            else:
                char = nums[i]
                count = 1

            if count == 3:
                nums.pop(i)
                i -= 1
                count -= 1
