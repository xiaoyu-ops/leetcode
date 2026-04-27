#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = len(matrix[0]) - 1
        
        while i<=len(matrix)-1 and j>=0:

            now = matrix[i][j]
            
            if now == target:
                return True
            if now>target:
                j -= 1
            else:
                i += 1
        
        return False
# @lc code=end

