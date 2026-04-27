#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def change(node):
            if not node:
                return 

            # 改变左子树和右子树 注意这个必须同时
            # 这样写就没问题了（针对不能写一行的问题）
            # old_left = node.left  # 先把旧的左子树存起来，防止丢失
            # node.left = change(node.right) 
            # node.right = change(old_left) # 这里使用的是保存好的旧左子树

            node.left,node.right = change(node.right),change(node.left)
            return node
            
        change(root)

        return root
# @lc code=end

