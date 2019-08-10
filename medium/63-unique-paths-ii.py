# https://leetcode.com/problems/unique-paths-ii/
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach
# the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?

from typing import List


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # 定义障碍物点，可通行点
        obstacle, walkable = 0, 1
        # 定义路径范围的高度，长度
        height, width = len(obstacleGrid), len(obstacleGrid[0])

        # 将障碍物定义为1改成定义为obstacle, 其余为walkable
        for h in range(height):
            for w in range(width):
                obstacleGrid[h][w] = obstacle if obstacleGrid[h][w] == 1 else walkable

        # 如果起点或者中点为障碍物点，则无法达到
        if obstacleGrid[0][0] is obstacle or obstacleGrid[-1][-1] is obstacle:
            return 0

        # 处理第一行，转化为路径值
        for w in range(1, width):
            # 如果前一个点为障碍物点，那么该点无法到达，视为障碍物点
            if obstacleGrid[0][w - 1] is obstacle:
                obstacleGrid[0][w] = obstacle

        # 处理第一列，转化为路径
        for h in range(1, height):
            # 如果前一个点为障碍物点，那么该点无法到达，视为障碍物点
            if obstacleGrid[h - 1][0] is obstacle:
                obstacleGrid[h][0] = obstacle

        for h in range(1, height):
            for w in range(1, width):

                # 根据当前点值进行判断
                if obstacleGrid[h][w] is obstacle:
                    # 如果当前点为障碍物，则到达该点有零条路径
                    continue
                else:
                    # 否则，到达当前点的路径值为dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    obstacleGrid[h][w] = obstacleGrid[h - 1][w] + obstacleGrid[h][w - 1]

        return obstacleGrid[-1][-1]
