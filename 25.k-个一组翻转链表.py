#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur,count = head,0
        while cur and count < k:
            cur = cur.next
            count += 1
        if count < k:
            return head

        # 翻转前 k 个节点
        prev,cur = None,head
        for _ in range(k):
            nxt = cur.next
            cur.next = prev
            prev,cur = cur,nxt
        
        # head就变成最后一个节点了 这个时候我们要接上后面的节点
        head.next = self.reverseKGroup(cur,k)
        return prev

# @lc code=end

