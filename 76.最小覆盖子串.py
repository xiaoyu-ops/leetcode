#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        check = dict()
        need = Counter(t)
        have,require = 0,len(need)
        left = 0
        result = ""
        min_len = float("inf")
        # 我们先一直向右边扩张 直到满足条件我们就收缩，注意考虑下一次扩张的时机
        
        for right in range(len(s)):
            str = s[right]
            check[str] = check.get(str,0) + 1
            if check[str] == need[str]:
                have += 1
            while have == require:
                str_delete = s[left]
                check[str_delete] = check.get(str_delete,0) - 1
                if check[str_delete] < need[str_delete]:
                    have -= 1
                    cur_result = s[left:right+1]
                    cur_len = len(cur_result)
                    if cur_len < min_len:
                        result = cur_result
                        min_len = cur_len
                    
                left += 1
            
        return result


# @lc code=end

