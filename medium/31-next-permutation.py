# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
#
# 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
#
# 必须原地修改，只允许使用额外常数空间。
#
# 以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/next-permutation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class SolutionNotMine:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # find the longest non-increasing suffix
        right = len(nums) - 1
        while right > 0 and nums[right - 1] >= nums[right]:
            right -= 1
        print('longest non-increasing suffix:', right)
        if right == 0:
            return nums.reverse()

        # identify the pivot - the last number in front of the suffix
        pivot = right - 1
        print('the pivot - the last number in front of the suffix:', pivot)

        # # find the rightmost number which is greater than the pivot in the suffix
        right = len(nums) - 1
        while nums[right] <= nums[pivot]:
            right -= 1
        print('rightmost number which is greater than the pivot in the suffix:', nums[right], 'suffix:', right)

        # swap pivot and the result
        nums[pivot], nums[right] = nums[right], nums[pivot]

        print(nums)

        # reverse the new suffix
        # l, r = pivot + 1, len(nums) - 1
        # while l < r:
        #     nums[l], nums[r] = nums[r], nums[l]
        #     l += 1
        #     r -= 1

        nums[pivot + 1:] = sorted(nums[pivot + 1:])

        print(nums)

        # return nums


class Solution3:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        for i in range(length - 1, 0 - 1, -1):
            i_length = len(nums[i:])
            for k in range(i_length):
                swap_index = self._get_swapable_index(nums[i:length - k])
                if swap_index != -1:
                    # 使用交换值更新原数组
                    nums[i + swap_index], nums[length - k - 1] = nums[length - k - 1], nums[i + swap_index]
                    # 排序
                    self._sort(nums, i + 1)
                    return

        nums.sort()

    def _get_swapable_index(self, nums: List[int]) -> int:
        """获得可交换值在数组的索引值；如果没有交换值，返回-1"""
        # print('before swap', nums)
        length = len(nums)
        for i in range(length - 2, -1, -1):
            if nums[length - 1] > nums[i]:
                # nums[length - 1], nums[i] = nums[i], nums[-1]
                # print('after swap:', nums, ', index:', i)
                return i
        return -1

    def _sort(self, nums: List[int], start: int) -> None:
        # print('before sort:', nums[start:], ', start:', start)
        nums[start:] = sorted(nums[start:])
        # print('after sort', nums[start:])


class Solution:

    def __init__(self):
        self._steps = 0

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0 - 1, -1):
            # print('1. nums[i:] -', nums[i:])
            for k in range(len(nums[i:])):
                # print('2. nums[i:len(nums) - k]', nums[i:len(nums) - k])
                check_nums = nums[i:len(nums) - k]
                swap_index = self._get_swapable_index(check_nums)
                if swap_index != -1:
                    # self._sort(check_nums, swap_index)
                    # 使用交换值更新原数组
                    nums[i:len(nums) - k] = check_nums
                    # 排序
                    self._sort(nums, i + 1)
                    return
        print(self._steps)
        nums.sort()

    def _get_swapable_index(self, nums: List[int]) -> int:
        """获得可交换值在数组的索引值；如果没有交换值，返回-1"""
        # print('before swap', nums)
        length = len(nums)
        for i in range(length - 2, -1, -1):
            self._steps += 1
            if nums[length - 1] > nums[i]:
                nums[length - 1], nums[i] = nums[i], nums[-1]
                # print('after swap:', nums, ', index:', i)
                return i
        return -1

    def _sort(self, nums: List[int], start: int) -> None:
        # print('before sort:', nums[start:], ', start:', start)
        nums[start:] = sorted(nums[start:])
        # print('after sort', nums[start:])


def main():
    nums_list = [
        [1, 2, 3, 4],
        [1, 2, 4, 3],
        [1, 3, 2, 4],
        [1, 3, 4, 2],
        [1, 4, 2, 3],
        [1, 4, 3, 2],
        [2, 1, 3, 4],
        [2, 1, 4, 3],
        [2, 3, 1, 4],
        [2, 3, 4, 1],
        [2, 4, 1, 3],
        [2, 4, 3, 1],
        [3, 1, 2, 4],
        [3, 1, 4, 2],
        [3, 2, 1, 4],
        [3, 2, 4, 1],
        [3, 4, 1, 2],
        [3, 4, 2, 1],
        [4, 1, 2, 3],
        [4, 1, 3, 2],
        [4, 2, 1, 3],
        [4, 2, 3, 1],
        [4, 3, 1, 2],
        [4, 3, 2, 1],
    ]

    answer = [
        [1, 2, 4, 3],
        [1, 3, 2, 4],
        [1, 3, 4, 2],
        [1, 4, 2, 3],
        [1, 4, 3, 2],
        [2, 1, 3, 4],
        [2, 1, 4, 3],
        [2, 3, 1, 4],
        [2, 3, 4, 1],
        [2, 4, 1, 3],
        [2, 4, 3, 1],
        [3, 1, 2, 4],
        [3, 1, 4, 2],
        [3, 2, 1, 4],
        [3, 2, 4, 1],
        [3, 4, 1, 2],
        [3, 4, 2, 1],
        [4, 1, 2, 3],
        [4, 1, 3, 2],
        [4, 2, 1, 3],
        [4, 2, 3, 1],
        [4, 3, 1, 2],
        [4, 3, 2, 1],
        [1, 2, 3, 4],
    ]
    # for i, nums in enumerate(nums_list):
    #     solution = Solution()
    #     solution.nextPermutation(nums)
    #     assert nums == answer[i], f'Wrong answer at index {i}, result: {nums}, expect: {answer[i]}'

    nums = [
        60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41,
        40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21,
        20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
    ]
    nums = [1, 3, 5, 4, 2]
    print(nums)
    solution = SolutionNotMine()
    solution.nextPermutation(nums)
    print(nums)


if __name__ == '__main__':
    main()
