#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
# 利用了前缀和以及字典
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int):
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        presum = 0
        count = 0
        for _ in nums:
            presum += _
            count += prefix_count[presum-k]
            prefix_count[presum] += 1

        return count
    # @lc code=end

