#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque 
        dp = deque()
        result = []
        for i in range(len(nums)):
            # 队头滑出窗口就弹出
            while dp and dp[0] < i - k + 1:
                dp.popleft()
            
            # 维护单调递减 当前元素更大则队尾永无出头之日
            while dp and nums[i] > nums[dp[-1]]:
                dp.pop()
            
            dp.append(i)

            if i >= k - 1:
                result.append(nums[dp[0]])
        return result
# @lc code=end

