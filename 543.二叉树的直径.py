#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxheight = 0
        def dfs(node):
            if not node:
                return 0
            
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            # 经过当前节点的直径
            self.maxheight = max(self.maxheight,left_depth+right_depth)
            return max(left_depth,right_depth) + 1 # 函数返回高度
        
        dfs(root)

        return self.maxheight
# @lc code=end

