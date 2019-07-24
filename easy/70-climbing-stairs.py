
# https://leetcode-cn.com/problems/climbing-stairs/
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。


class Solution:
    # dp[i] = dp[i - 1] + dp[i - 2]
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0, 1, 2]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        # dp.append(dp[-1] + dp[-2])
        return dp[-1]


if __name__ == '__main__':
    n = 10
    solution = Solution()
    m = solution.climbStairs(n)
    print(m)
