#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(path,left,right):
            if len(path) == 2 * n:
                result.append(''.join(path))
                return 
            if left < n:
                path.append('(')
                backtrack(path,left + 1,right)
                path.pop()
            if right < left:
                path.append(')')
                backtrack(path,left,right + 1)
                path.pop()
        path = []
        backtrack(path,0,0)
        return result

# @lc code=end

