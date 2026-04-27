#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxroad = -math.inf

        def dfs(node):
            if not node:
                return 0
            # 注意负收益不如不走
            left_road =  max(dfs(node.left),0)
            right_road = max(dfs(node.right),0)
            # 补充一个关于不一定经过根节点的处理
            self.maxroad = max(self.maxroad,left_road + right_road + node.val)
            return node.val + max(left_road,right_road)
        dfs(root)
        return self.maxroad
# @lc code=end

