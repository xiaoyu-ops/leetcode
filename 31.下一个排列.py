#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2

        # 从右找第一个下降点；若全降序则已是最大排列
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # 从右找第一个比 nums[i] 大的数（"刚好大一点"）并交换
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 翻转 i+1 到末尾：降序变升序，得到最小后缀
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
# @lc code=end

