#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i]我们可以看作前i个字符能否被切分的情况。
        n = len(s)
        dp = [False] * (n+1)
        word_set = set(wordDict)
        dp[0] = True
        # 可选优化：限制回看长度
        max_len = max((len(w) for w in word_set), default=0)

        # 外层循环其实是判断dp[i]的即前缀
        # 内层其实是不断在移动j的切分位置
        for i in range(1, n + 1):
            # j 是最后一刀的位置，检查 s[j:i]
            # 此处我们希望j从i-max_len处开始，但是当i很小时
            # i-max_len这个值可能为负数
            start = max(0, i - max_len)
            for j in range(start, i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


# @lc code=end

