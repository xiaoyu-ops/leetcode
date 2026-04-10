#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 定义好prev,cur,next_node就行
        dummy = ListNode(0,head)
        prev = dummy
        while prev and prev.next:
            a = prev.next
            b = prev.next.next
            if not b:
                return dummy.next
            # 交换
            prev.next = b
            a.next = b.next
            b.next = a
            prev = a # 将 prev 移动到交换后第二个节点

        return dummy.next
# @lc code=end

