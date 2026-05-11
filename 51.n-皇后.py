#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        用三个 set 记录列/正对角线(row-col)/反对角线(row+col)冲突，O(1) 判断。
        按行递归，每行只放一个皇后，天然避免行冲突。
        """
        result = []
        cols = set()
        diag1 = set()
        diag2 = set()

        def backtrack(row, path):
            if row == n:
                result.append([''.join(r) for r in path])
                return
            for col in range(n):
                if col in cols or (row-col) in diag1 or (row+col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row-col)
                diag2.add(row+col)
                path.append(['.' if c != col else 'Q' for c in range(n)])
                backtrack(row + 1, path)
                path.pop()
                cols.discard(col)
                diag1.discard(row-col)
                diag2.discard(row+col)

        backtrack(0, [])
        return result
# @lc code=end

