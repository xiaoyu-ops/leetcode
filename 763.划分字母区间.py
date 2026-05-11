#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        check = {}
        for i in range(len(s)):
            check[s[i]] = i
        ans = []
        idx = 0
        left = 0
        for i in range(len(s)):
            left = max(left,check[s[i]])
            if i == left:
                ans.append(len(s[idx:i + 1]))
                idx = i + 1
        return ans
# @lc code=end

