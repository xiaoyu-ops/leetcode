#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = []
        rows = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    cols.append(j)
                    rows.append(i)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        
# @lc code=end

