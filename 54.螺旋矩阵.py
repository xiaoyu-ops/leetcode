#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        down = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        ans = []
        while left<=right and top<=down:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top +=1

            for i in range(top,down+1):
                ans.append(matrix[i][right])
            right -=1

            if top<=down:
                for i in range(right,left-1,-1):
                    ans.append(matrix[down][i])
                down -=1

            if left<=right:
                for i in range(down,top-1,-1):
                    ans.append(matrix[i][left])
                left +=1
        return ans
# @lc code=end

