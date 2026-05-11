#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if max_reach < i:
                return False
            cur_reach = i + nums[i]
            max_reach = max(max_reach,cur_reach)
            if max_reach >= len(nums) - 1:
                return True
        return False
# @lc code=end

