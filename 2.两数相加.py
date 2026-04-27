#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        add = 0

        # 逐位相加，处理进位；链表不等长时用 0 补齐
        while l1 or l2 or add:
            val = add
            add = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            if val >= 10:
                add = 1
                val = val%10
            cur.next = ListNode(val)
            cur = cur.next

        return dummy.next
        

# @lc code=end

