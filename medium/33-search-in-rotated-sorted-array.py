# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


# 思路 -
# 将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序；
# 此时有序部分用二分法查找；
# 无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环.
class SolutionTodo:

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1

            if nums[mid] > nums[right]:
                if nums[mid] < target and nums[right] >= target:
                    pass


            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[mid] > target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


class SolutionNotMine:

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[mid] > target and nums[left] <= target:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


class SolutionMine:

    def search(self, nums: List[int], target: int) -> int:
        # 数组为空，返回-1
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        # 寻找中轴点
        pivot = self._find_reverse_pivot(nums, left, right)
        # 如果中轴索引为目标值，直接返回中轴值
        if nums[pivot] == target:
            return pivot

        return max(
            self._find_target(nums, left, pivot - 1, target) if pivot - 1 >= left else -1,
            self._find_target(nums, pivot + 1, right, target) if pivot + 1 <= right else -1)

    def _find_reverse_pivot(self, nums: List[int], left, right) -> int:
        """关键点：中轴必然位于左值大于右值的范围内"""
        mid = (left + right) >> 1
        l_left, l_right = left, mid - 1
        r_left, r_right = mid + 1, right
        if l_left < l_right and nums[l_left] > nums[l_right]:
            return self._find_reverse_pivot(nums, l_left, l_right)
        elif r_left < r_right and nums[r_left] > nums[r_right]:
            return self._find_reverse_pivot(nums, r_left, r_right)
        else:
            return min(mid, mid + 1, key=lambda i: nums[i]) if mid + 1 <= right else mid

    def _find_target(self, nums: List[int], left: int, right: int, target: int) -> int:
        """Binary search to find target"""
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left if nums[left] == target else -1




def main():
    target = 1
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    nums = [21, 33, 44, 57, 68, 79, 81, 96, 12]
    nums = [8, 9, 0, 1, 2, 3, 4, 5, 6, 7]
    nums = []
    solution = SolutionMine()
    result = solution.search(nums, target)
    print(result)
    # print('index:', result, 'num', nums[result])


if __name__ == '__main__':
    main()
