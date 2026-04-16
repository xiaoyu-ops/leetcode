#
# @lc app=leetcode.cn id=84 lang=python3
#
# [84] 柱状图中最大的矩形
#

from typing import List

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        # 构建一个单调递增栈，每个柱子弹出的时候计算以其为高度的最大矩形
        stack = [0] # 存索引
        max_area = 0
        for i in range(1,len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                current_area = heights[idx] * (i - stack[-1] - 1)
                max_area = max(current_area,max_area)
            stack.append(i)
        return max_area
# @lc code=end

