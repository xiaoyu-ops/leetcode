#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0,len(height)-1
        # 左右两边一直收缩直到相遇 ，然后这个
        # 过程中我们不断记录这个 max就行
        max_vol = 0
        while left < right:
            cur_vol = (right-left)*min(height[left],height[right])
            max_vol = max(max_vol,cur_vol)

            # 每次移动比较矮的那一侧
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_vol
# @lc code=end

