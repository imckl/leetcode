# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的绝对值最大为 k。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/contains-duplicate-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List
from collections import OrderedDict


class Solution(object):
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = OrderedDict()

        for i, num in enumerate(nums):
            if num in window and i - window[num] <= k:
                return True
            window[num] = i

        return False


class Solution3(object):
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        sliding_window = []
        for num in nums:
            if num in sliding_window:
                return True
            sliding_window.append(num)
            if len(sliding_window) > k:
                sliding_window.pop(0)

        return False


class Solution2(object):
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i, num in enumerate(nums):
            if num is None:
                continue

            check_list = [j for j, num2 in enumerate(nums[i:]) if num2 == nums[i]]
            if self._is_meet_condition(check_list, k):
                return True

            for j in check_list:
                nums[j + i] = None

        return False

    def _is_meet_condition(self, check_list: List[int], k: int) -> bool:
        for i in range(len(check_list) - 1):
            if check_list[i + 1] - check_list[i] <= k:
                return True
        return False


def main():
    nums = [1, 2, 3, 1]
    k = 5
    nums = [i for i in range(100000)]
    k = 100000
    # nums = [0,1,2,3,4,5,0]
    # nums = [i for i in range(0, 10000, 5)]
    # k = 2
    solution = Solution()
    result = solution.containsNearbyDuplicate(nums, k)
    print(result)


if __name__ == '__main__':
    main()
