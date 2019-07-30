# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of
# the non-zero elements.
# https://leetcode.com/problems/move-zeroes/

from typing import List


class Solution(object):
    def moveZeroes(self, nums: List[int]):
        not_zero_count = 0
        for num in nums:
            if num != 0:
                nums[not_zero_count] = num
                not_zero_count += 1

        nums[not_zero_count:] = [0] * len(nums[not_zero_count:])


class Solution3(object):
    def moveZeroes(self, nums: List[int]):
        count = 0
        while True:
            try:
                nums.remove(0)
                count += 1
            except ValueError:
                break
        for _ in range(count):
            nums.append(0)


class Solution2(object):
    def moveZeroes(self, nums: List[int]):
        zero_count = nums.count(0)

        if not zero_count:
            return

        move_count = 0
        length = len(nums)

        while zero_count:
            zero_index = nums.index(0, 0, length - move_count)
            nums.append(0)
            nums.pop(zero_index)
            zero_count -= 1
            move_count += 1


def main():
    nums = [0, 1, 0, 3, 12]
    solution = Solution()
    solution.moveZeroes(nums)
    print(nums)


if __name__ == '__main__':
    main()
