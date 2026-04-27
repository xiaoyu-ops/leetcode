#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return 
        elif len(lists) < 2:
            return lists[0]

        ans = lists[0] 
        for i in range(1,len(lists)):
            ans = self._merge(ans,lists[i])
        return ans
    
    def _merge(self,l1,l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next,l1 = l1,l1.next
            else:
                cur.next,l2 = l2,l2.next
            cur = cur.next

        cur.next = l1 if l1 else l2
        return dummy.next
            
# @lc code=end

