#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # rows = len(matrix)-1
        # cols = len(matrix[0])-1
        # i = 0
        # j = cols
        # while i<=rows and j>=0:
        #     if matrix[i][j] == target:
        #         return True
        #     if matrix[i][j] > target:
        #         j -= 1
        #     else:
        #         i += 1
        # return False
        
        # 用二分查找的方法
        m = len(matrix)
        n = len(matrix[0])
        left,right = 0,m*n-1
        while left <= right:
            mid = left + (right - left)//2
            # 处理列号和行号,每行有 n 个元素，整除法得到
            # 在第几行 以及 取余得到在哪列
            row,col = mid//n , mid%n
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
# @lc code=end

