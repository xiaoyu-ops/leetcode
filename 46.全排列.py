#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def backtrack(path,nums):
            if len(nums) == len(path):
                ans.append(path[:])
                return 

            for choice in nums:
                if choice in path:
                    continue
                path.append(choice)
                backtrack(path,nums)
                path.pop()

        backtrack(path,nums)
        return ans
# @lc code=end

