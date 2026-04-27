#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for i,num in enumerate(nums):
            # i是索引，num 是对应的值
            diff = target - num
            if diff in check:
                return [check[diff],i]
            check[num] = i
# @lc code=end

