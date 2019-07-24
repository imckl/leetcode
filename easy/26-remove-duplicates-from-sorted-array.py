
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
from collections import OrderedDict


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        i = 0
        while True:
            try:
                if nums[i] == nums[i + 1]:
                    nums.pop(i)
                else:
                    i += 1
            except IndexError:
                break
        return len(nums)

    def removeDuplicates2(self, nums: List[int]) -> int:
        nums[:] = OrderedDict.fromkeys(nums)
        return len(nums)


if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    solution = Solution()
    m = solution.removeDuplicates(nums)
    print(m)
