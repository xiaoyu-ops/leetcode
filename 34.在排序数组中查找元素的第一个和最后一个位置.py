#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left,right = 0,len(nums)-1
        def find_left(left,right):

            while left <= right:
                mid = (right - left)//2 + left
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left if left<len(nums) and nums[left] == target else -1

        def find_right(left,right):

            while left <= right:

                mid = (right - left)//2 + left
                
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            
            return right if right>=0 and nums[right] == target else -1   

        return [find_left(left,right),find_right(left,right)]     
# @lc code=end

