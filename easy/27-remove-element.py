
# https://leetcode.com/problems/remove-element/
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.

from typing import List
from collections import OrderedDict


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while True:
            try:
                if nums[i] == val:
                    nums.pop(i)
                else:
                    i += 1
            except IndexError:
                break

        return len(nums)

    def removeElement2(self, nums, val):
        while val in nums:
            nums.remove(val)



if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    solution = Solution()
    m = solution.removeElement(nums, 2)
    print(m)
