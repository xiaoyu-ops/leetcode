#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 二分查找 一定有一边肯定是有序的
        left,right = 0,len(nums)-1
        while left < right:
            # 最后出来的时候 left和right是一个值
            mid = left + (right - left)//2

            if nums[mid] > nums[right]:
                # 说明递增的在左边,断崖点在右边
               left = mid + 1
            else:
                # 往左收缩
                right = mid # 因为 mid 也有可能是最小值
        
        return nums[left] 
# @lc code=end

