
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
#
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/single-number
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        for i in nums:
            if dic.get(i) == 1:
                return i


class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n % 2 == 0: return None
        ans = 0
        for e in nums:
            ans ^= e
        return ans


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)


if __name__ == '__main__':
    nums = [2 , 2, 1]
    s = Solution()
    r = s.singleNumber(nums)
    print(r)