#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        # 1.BFS广度优先搜索的写法
        # # 先做可达性剪枝：如果 amount 不是所有 coin 的 gcd 的倍数，必定无解
        # g = 0
        # # 求所有硬币面值的最大公约数
        # for c in coins:
        #     g = math.gcd(g, c)
        # if amount % g != 0:
        #     return -1

        # # BFS 按“使用硬币个数”分层，第一次到达 0 就是最少硬币数
        # now_level = {amount}
        # visited = {amount}
        # steps = 0

        # while now_level:
        #     steps += 1
        #     next_level = set()
        #     for cur in now_level:
        #         for c in coins:
        #             nxt = cur - c
        #             if nxt == 0:
        #                 return steps
        #             if nxt > 0 and nxt not in visited:
        #                 visited.add(nxt)# 处理跨层全局去重
        #                 next_level.add(nxt)
        #     now_level = next_level

        # return -1

        # 2.动态规划（标准写法）
        # dp[i] 表示凑出金额 i 所需的最少硬币数
        inf = amount + 1
        dp = [inf] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return -1 if dp[amount] == inf else dp[amount]

# @lc code=end

