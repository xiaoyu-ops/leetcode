#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start_1,start_2 = list1,list2
        dummy = ListNode()
        ans = dummy
        while start_1 and start_2:
            if start_1.val >= start_2.val:
                ans.next = start_2
                start_2 = start_2.next

            else:
                ans.next = start_1
                start_1 = start_1.next
            ans = ans.next
        
        if not start_1:
            ans.next = start_2
        else:
            ans.next = start_1

        return dummy.next

# @lc code=end

