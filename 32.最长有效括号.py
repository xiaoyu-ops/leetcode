#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
    # 关于本题我们先想一下，dp[i]具体代表什么？dp[i]代表第i个字符结尾的
    # 时候最长有效括号的长度
        if len(s) == 0:
            return 0
        n = len(s)
        if n < 2: return 0
        
        dp = [0] * n
        res = 0
        
        for i in range(1, n):
            if s[i] == ')':
                # 情况 1: s[i-1] 是 '('，直接凑成一对
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                
                # 情况 2: s[i-1] 也是 ')'，找它前面的对应位置
                elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(':
                    # 计算公式：内部长度 + 2 + 外部连接长度
                    prev_idx = i - dp[i-1] - 2
                    dp[i] = dp[i-1] + 2 + (dp[prev_idx] if prev_idx >= 0 else 0)
                    
                res = max(res, dp[i])
                
        return res
# @lc code=end

