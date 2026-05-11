#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 先合并
        ans = []
        m,n = len(nums1),len(nums2)
        i,j = 0,0

        while i<m and j<n:
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        if i == m:
            for x in range(j,len(nums2)):
                ans.append(nums2[x])
        else:
            for x in range(i,len(nums1)):
                ans.append(nums1[x])
        
        if (len(ans)-1)%2==0:
            mid = (len(ans)-1)//2
            return ans[mid]
        else:
            mid = (len(ans)-1)//2
            return (ans[mid] + ans[mid+1])/2


        # # 在较短的数组上二分，减少搜索范围
        # if len(nums1) > len(nums2):
        #     nums1, nums2 = nums2, nums1

        # m, n = len(nums1), len(nums2)
        # half = (m + n) // 2

        # # i：nums1 的切割点（i 个元素在左半部分）
        # # j：nums2 的切割点，由 half 推导
        # lo, hi = 0, m
        # while lo <= hi:
        #     i = (lo + hi) // 2
        #     j = half - i

        #     # 切割点周围的四个值，越界用无穷代替
        #     nums1_left  = nums1[i - 1] if i > 0 else float('-inf')
        #     nums1_right = nums1[i]     if i < m else float('inf')
        #     nums2_left  = nums2[j - 1] if j > 0 else float('-inf')
        #     nums2_right = nums2[j]     if j < n else float('inf')

        #     # 切割正确：左半所有值 ≤ 右半所有值
        #     if nums1_left <= nums2_right and nums2_left <= nums1_right:
        #         if (m + n) % 2 == 1:
        #             return float(min(nums1_right, nums2_right))
        #         else:
        #             return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0

        #     # nums1 左边元素太多，切割点左移
        #     if nums1_left > nums2_right:
        #         hi = i - 1
        #     # nums1 左边元素太少，切割点右移
        #     else:
        #         lo = i + 1

# @lc code=end

