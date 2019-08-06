# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


# 作者：liweiwei1419
# 链接：https://leetcode-cn.com/problems/two-sum/solution/si-lu-hen-jian-dan-xi-jie-fei-mo-gui-de-er-fen-cha/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class SolutionNotMine:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        # 特判，这一步很重要，否则执行到后序方法可能会出现数组下标越界
        # 同时后序两个方法也不用做特殊判断了
        if size == 0:
            return [-1, -1]

        num1 = self.__find_lower_bound(nums, target)
        # 细节：如果左边界都搜索不到，右边界也没有必要看了
        if num1 == -1:
            return [-1, -1]

        num2 = self.__find_up_bound(nums, target)
        return [num1, num2]

    def __find_lower_bound(self, nums, target):
        # 找等于 target 的第 1 个数的索引，小于一定不符合要求
        size = len(nums)

        left = 0
        right = size - 1
        while left < right:
            # 根据分支逻辑，这里选择左中位数
            # mid = left + (right - left) // 2
            mid = (left + right) >> 1
            # 因为找大于等于 target 的第 1 个数，因此小于一定不符合要求
            # 把它写在分支的前面
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        # 因为有可能不存在目标元素，最后一定要单独判断一下
        if nums[left] != target:
            return -1
        return left

    def __find_up_bound(self, nums, target):
        # 找等于 target 的最后 1 个数的索引，大于一定不符合要求
        # 因为有可能不存在，最后一定要单独判断一下
        size = len(nums)
        left = 0
        right = size - 1
        while left < right:
            # 根据分支逻辑，这里选择右中位数
            # mid = left + (right - left + 1) // 2
            mid = (left + right + 1) >> 1
            # 因为找小于等于 target 的最后 1 个数，因此大于一定不符合要求
            # 把它写在分支的前面
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid
        # 因为有可能不存在目标元素，最后一定要单独判断一下
        if nums[left] != target:
            return -1
        return left


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        left: int = 0
        right: int = len(nums) - 1

        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        # print('left:', left, 'right:', right, 'nums[left]:', nums[left], 'target', target)
        if nums[left] == target:
            mid = left
        else:
            return [-1, -1]

        min_idx, max_idx = left, left

        tmp_min_idx = self._bs(nums, 0, mid - 1, target)
        while tmp_min_idx != -1:
            min_idx = tmp_min_idx
            tmp_max_idx = self._bs(nums, 0, tmp_min_idx - 1, target)

        tmp_max_idx = self._bs(nums, mid + 1, len(nums) - 1, target)
        while tmp_max_idx != -1:
            max_idx = tmp_max_idx
            tmp_max_idx = self._bs(nums, tmp_max_idx + 1, len(nums) - 1, target)

        return [min_idx, max_idx]

    def _bs(self, nums: List[int], left: int, right: int, target: int) -> int:
        # print('_bs:', 'left:', left, 'right:', right)
        if left > right:
            return -1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        result = left if nums[left] == target else -1
        # print('_bs:', 'nums[left]:', nums[left], 'target:', target, 'result:', result)
        return result


def main():
    target = 8
    nums = []
    solution = Solution()
    result = solution.searchRange(nums, target)
    print(result)


if __name__ == '__main__':
    main()
