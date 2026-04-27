#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
                # 核心就是层序遍历
        def bfs(node):
            if not node:
                return []
            
            queue = deque([node])
            result = []

            while queue:
                level_size = len(queue) # 当前节点的层数
                level = []
                for _ in range(level_size):
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                result.append(level[-1])
            return result

        result = bfs(root)
        return result

# @lc code=end

