#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = []
        for i in range(numRows):
            row = [1] * (i+1)
            for j in range(1,i):
                row[j] = dp[i-1][j-1] + dp[i-1][j]
            dp.append(row)
        return dp

# @lc code=end

