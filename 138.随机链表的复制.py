#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 随机链表的复制
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 我的理解就是完全复制一下这个新链表包含 next，val，random 那些
        check = {}
        cur = head
        while cur:
            # 注意直接存节点更方便
            check[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        check[None] = None

        while cur:
            next_node = cur.next
            random_node = cur.random
            check[cur].next = check[next_node]
            check[cur].random = check[random_node]
            cur = cur.next
        return check[head]
# @lc code=end

