#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 先找中点
        if not head or not head.next:
            return head
        
        slow,fast = head,head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow.next
        slow.next = None
        # 断成两段

        left = self.sortList(head)
        right = self.sortList(mid)
        return self._merge(left,right)
    
    def _merge(self,l1,l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next,l1 = l1,l1.next
            else:
                cur.next,l2 = l2,l2.next
            cur = cur.next
        cur.next = l1 or l2# 取决于谁没走到最后
        return dummy.next

# @lc code=end

