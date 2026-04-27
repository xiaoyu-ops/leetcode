#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefix = {}
        prefix[0] = 1
        def dfs(node,cur_sum):
            if not node:
                return 0
            
            cur_sum += node.val

            count = prefix.get(cur_sum - targetSum,0)

            prefix[cur_sum] = prefix.get(cur_sum,0) + 1
            
            count += dfs(node.left,cur_sum)
            count += dfs(node.right,cur_sum)

            # 注意路径是向下的不能共享一条同根到该节点的路径
            prefix[cur_sum] -= 1
            return count
        return dfs(root,0)
# @lc code=end

