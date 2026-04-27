#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count +=1 
                    self.dfs(grid,i,j)
        return count

    def dfs(self,grid,i,j):
        # 越界或已访问/水域就返回
        if i<0 or i >= len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "0"
        for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            self.dfs(grid,i+di,j+dj)
# @lc code=end

