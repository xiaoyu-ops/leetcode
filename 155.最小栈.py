#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
from collections import deque
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val,self.minstack[-1]) if self.minstack else val
        self.minstack.append(min_val)        

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        ans = self.stack[-1]
        return ans

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

