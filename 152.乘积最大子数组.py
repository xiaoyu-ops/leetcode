#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
import math
# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 状态初始化：以下标 0 结尾的子数组，只有 nums[0] 自己
        dp_max = nums[0]   # 以当前位置结尾的最大乘积
        dp_min = nums[0]   # 以当前位置结尾的最小乘积
        ans = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            prev_max, prev_min = dp_max, dp_min

            # 状态转移：三选一
            dp_max = max(x, prev_max * x, prev_min * x)
            dp_min = min(x, prev_max * x, prev_min * x)

            ans = max(ans, dp_max)

        return ans


# @lc code=end

