#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        result = []
        def backtrack(start,choice,path):# 加个 start 不允许回头 防止重复的情况
            if sum(path) == target:
                result.append(path[:])
                return
            
            if sum(path) > target:
                return 
            
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                backtrack(i,choice,path)
                path.pop()
        
        backtrack(0,candidates,path)
        
        return result

# @lc code=end

