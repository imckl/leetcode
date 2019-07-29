
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/house-robber
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from typing import List

# Step 1. Figure out recursive relation.
# A robber has 2 options: a) rob current house i; b) don't rob current house.
# dp[i] = max(dp[i - 2] + house_rob_value, dp[i - 1])
# 1. Find recursive relation
# 2. Recursive (top-down)
# 3. Recursive + memo (top-down)
# 4. Iterative + memo (bottom-up)
# 5. Iterative + N variables (bottom-up)


class Solution(object):
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        prev_max, curr_max = 0, 0
        for num in nums:
            # tmp = curr_max
            # curr_max = max(prev_max + num, curr_max)
            # prev_max = tmp
            prev_max, curr_max = curr_max, max(prev_max + num, curr_max)

        return curr_max


# Step 4. Iterative + memo (bottom-up)
class SolutionStep4(object):
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        memo = [0, nums[0]]
        for i in range(1, len(nums)):
            memo.append(max(memo[i], memo[i - 1] + nums[i]))

        return memo[-1]


# Step 3. Recursive + memo (top-down).
# Time: O(n), Space: O(n)
class SolutionStep3(object):
    def __init__(self):
        self._memo = []

    def rob(self, nums: List[int]) -> int:
        self._memo[:] = [-1 for _ in range(len(nums) + 1)]
        return self._rob(nums, len(nums) - 1)

    def _rob(self, nums: List[int], length: int) -> int:
        if length < 0:
            return 0

        # 记录了之前计算的值，避免重复计算
        if self._memo[length] >= 0:
            return self._memo[length]

        result = max(self._rob(nums, length - 2) + nums[length], self._rob(nums, length - 1))
        self._memo[length] = result

        return result


# Step 2. Recursive (top-down)
# Converting the recurrent relation from Step 1 shound't be very hard.
# Time, Space: to fill
class SolutionStep2(object):
    def rob(self, nums: List[int]) -> int:
        return self._rob(nums, len(nums) - 1)

    def _rob(self, nums: List[int], length: int) -> int:
        if length < 0:
            return 0
        return max(self._rob(nums, length - 2) + nums[length], self._rob(nums, length - 1))


def main():
    nums = [1,2,3,1]
    nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
    solution = Solution()
    result = solution.rob(nums)
    print(result)


if __name__ == '__main__':
    main()
