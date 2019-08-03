# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum-closest
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List, Optional


class Solution(object):

    def threeSumClosest(self, nums: List[int], target: int) -> int:

        length = len(nums)

        # 最接近的算术和，默认为正无穷
        nearest_sum = float('inf')

        # 排序后可使用双指针
        nums.sort()

        for i in range(length - 2):

            # 排除重复计算
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 双指针法
            left, right = i + 1, length - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]

                # 更新算术和
                if abs(target - sum_) < abs(target - nearest_sum):
                    nearest_sum = sum_

                # 无论是左指针右移，还是右指针左移，都能够减少sum_与target的绝对值，即缩小距离
                if sum_ < target:
                    left += 1
                elif sum_ > target:
                    right -= 1
                else:
                    # 如果等于target, 则为最接近的情况，根据题意，返回以求得的最接近算术和
                    return nearest_sum

        return nearest_sum
