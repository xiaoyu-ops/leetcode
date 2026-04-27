#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 利用滑动窗口的思路
        window = {}
        left = 0
        max_len = 0
        
        for right in range(len(s)):
            if s[right] in window and window[s[right]] >= left:
                left = window[s[right]] + 1

            window[s[right]] = right
            max_len = max(max_len,right-left+1)
        return max_len 
# @lc code=end

