#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
from collections import deque
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        check = deque()
        for i in s:
            if i == '(' or i == '[' or i == '{':
                check.append(i)
            elif (i == ')' or i == ']' or i == '}') and len(check) == 0:
                return False
            if i == ')' and check[-1] == '(':
                check.pop()
            elif i == ']' and check[-1] == '[':
                check.pop()
            elif i == '}' and check[-1] == '{':
                check.pop()
            elif i == ')' or i == ']' or i == '}':
                return False
        return not check
# @lc code=end

