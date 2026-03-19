#
# @lc app=leetcode.cn id=624 lang=python3
#
# [624] 数组列表中的最大距离
#
from typing import List
# @lc code=start
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        ans = 0

        for arr in arrays[1:]:
            # 先和“之前数组”的最值比较，保证两个数来自不同数组
            # 关键就在于只提供了一个端点来进行比较
            ans = max(ans, arr[-1] - min_val, max_val - arr[0])
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])

        return ans
# @lc code=end

