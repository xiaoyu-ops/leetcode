#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果节点到底了就返回 或者节点就是我们要找的也返回
        if not root or root == p or root == q:
            return root
        
        # 找右子树看有没有
        left =  self.lowestCommonAncestor(root.left,p,q)
        # 找左子树看有没有
        right = self.lowestCommonAncestor(root.right,p,q)

        # 如果左右都找到一个那么我们当前节点就是共同祖先
        if left and right:
            return root
        
        # 如果只在一侧找到 p，q 都在同侧就继续上传
        return left or right
# @lc code=end

