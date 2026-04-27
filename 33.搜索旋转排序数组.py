#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0,len(nums)-1
        
        while left <= right:
            mid = (right-left)//2 + left
            # 判断我们的 target 是否落在了有序的一半
            if nums[mid] == target:
                return mid

            # 先判断哪边是有序的
            is_left = True if nums[left] <= nums[mid] else False

            if is_left:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 
                else:
                    right = mid - 1
        return -1
# @lc code=end

