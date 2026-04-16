#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

from typing import List

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 构建单调栈
        stack = []  # 存索引，栈内对应的值保持单调递增
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)
        return result
# @lc code=end

