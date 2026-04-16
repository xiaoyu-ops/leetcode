#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
import heapq
class MedianFinder:

    def __init__(self):
        # 大顶堆存小的一半，小顶堆存大的一半 这样大顶堆的最大的衔接小顶堆最小的
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        # 先入大顶堆
        heapq.heappush(self.big,-num)
        # 平衡 如果大顶堆的最大值大于小顶堆最小值就移过去
        if self.small and self.small[0] < (-self.big[0]):
            heapq.heappush(self.small,-heapq.heappop(self.big))
        if len(self.big) < len(self.small):
            heapq.heappush(self.big,-heapq.heappop(self.small))
        elif len(self.big) > len(self.small) + 1:
            heapq.heappush(self.small,-heapq.heappop(self.big))

    def findMedian(self) -> float:

        if len(self.small) == len(self.big):
            return (-self.big[0] + self.small[0]) / 2.0
        
        return -self.big[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

