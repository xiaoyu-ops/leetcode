#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第 K 小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = []
        self.account = 0
        self.res = None
        def dfs(node):
            if not node or self.res is not None:
                return 
            dfs(node.left)
            self.ans.append(node.val)
            self.account += 1
            if self.account == k:
                self.res = node.val
            dfs(node.right)
        
        dfs(root)
        return self.res
        # return self.ans[k-1]
# @lc code=end

