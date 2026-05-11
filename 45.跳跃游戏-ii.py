#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        current_end：当前跳跃能覆盖的最远边界；farthest：范围内下一跳的最远边界。
        到达 current_end 时必须再起跳，并将边界更新为 farthest。
        """
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
# @lc code=end

