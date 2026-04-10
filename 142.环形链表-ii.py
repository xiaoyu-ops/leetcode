#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        fast,slow = head,head
        if not fast.next:
            return None
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if fast != slow:
            return None
        # 我们设起点距离入环点为 x，相遇点距入环点为 y
        # 距出环点为z 那么 x + y + z = 链表节点数
        # 第一次相遇 slow走了至少 x+y 那么那么fast则是2(x+y)
        # 又因为fast肯定是套了slow整圈所以 fast-slow=x+y=y+z
        # 所以同速情况下肯定是相遇在入环点
        start_1 = head
        while start_1 != slow:
            start_1 = start_1.next
            slow = slow.next
        return slow
# @lc code=end

