#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow,fast = nums[0],nums[0]
        check = 0
        while slow != fast or check == 0:
            check  = 1
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
        
        # 相遇时 slow和 fast 在同一节点 这个时候把 slow 放回起始点再来就行
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow            
# @lc code=end

