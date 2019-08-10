# https://leetcode-cn.com/problems/unique-paths/


class Solution2:

    def uniquePaths(self, m: int, n: int) -> int:

        # 状态转移方程
        # dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # 创建dp表
        dp = [[1] * m] + [[1] + [0] * (m - 1) for _ in range(n - 1)]

        # 填充dp表
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:

        cur = [1] * n
        print(cur)

        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]
                print(cur)

        return cur[-1]


def main():
    m = 3
    n = 4
    solution = Solution()
    result = solution.uniquePaths(m, n)
    print(result)


if __name__ == '__main__':
    main()
