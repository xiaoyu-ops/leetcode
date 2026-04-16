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
        if len(lists) == 0:
            return None
        if len(lists) < 2:
            return lists[0] 
        first = self._merge(lists[0],lists[1])
        for i in range(2,len(lists)):
            first = self._merge(first,lists[i])
        return first
    
    def _merge(self,l1,l2):   
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
               cur.next,l1 = l1,l1.next
            else:
               cur.next,l2 = l2,l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
        
            
# @lc code=end

