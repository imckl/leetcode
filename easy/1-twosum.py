
# https://leetcode-cn.com/problems/two-sum/
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/two-sum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

class Solution:
    def twosum(self, nums: List[int], target: int) -> List[int]:
    # def twosum(nums, target):
        for i, x in enumerate(nums):
            if target - x in nums[i + 1:]:
                i2 = nums.index(target - x, i + 1)
                return [i, i2]


if __name__ == '__main__':
    # target = 10
    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    # target = 6
    # nums = [3, 2, 4]
    target = 6
    nums = [3, 3]
    s = Solution()
    print(s.twosum(nums, target))
