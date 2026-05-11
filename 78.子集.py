#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start,path):
            result.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                start += 1
                backtrack(start,path)
                path.pop()
        path = []
        backtrack(0,path)
        return result
# @lc code=end

