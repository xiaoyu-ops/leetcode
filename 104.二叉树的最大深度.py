#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            left_deepth = dfs(node.left)
            right_deepth = dfs(node.right)
            return max(left_deepth,right_deepth) + 1
        depth = dfs(root)
        return depth
# @lc code=end

