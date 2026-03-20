#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
from typing import List

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 依旧用dp[i][j]来表示到达i,j点处的最小数字总和
        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        rows = len(grid)
        cols = len(grid[0])
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, cols):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[rows - 1][cols - 1]
# @lc code=end

