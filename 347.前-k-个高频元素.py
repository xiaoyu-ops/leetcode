#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = {}
        heap,ans = [],[]
        for i in nums:
            check[i] = check.get(i,0) + 1
        
        for key,val in check.items():
            heapq.heappush(heap,(-val,key))
        
        for i in range(k):
            val,key = heapq.heappop(heap)
            ans.append(key)
        return ans

        
# @lc code=end

