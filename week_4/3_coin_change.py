# https://leetcode.com/problems/coin-change/
from typing import List


# Bottom-up dp solution
class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for curr_amt in range(1, amount + 1):
            for coin in coins:
                if curr_amt - coin >= 0:
                    dp[curr_amt] = min(dp[curr_amt], 1 + dp[curr_amt - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1


# Top-down approach
class Solution2:
    def helper(self, coins: List[int], curr_amt: int, amt: int, dp: List[int]) -> int:
        if dp[curr_amt] != amt + 1:
            return dp[curr_amt]
        for coin in coins:
            need_amt = curr_amt - coin
            if need_amt >= 0:
                dp[curr_amt] = min(dp[curr_amt], 1 + self.helper(coins, need_amt, amt, dp))
        return dp[curr_amt]

    def coin_change(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        result = self.helper(coins, amount, amount, dp)
        return result if result != amount + 1 else -1


def test_coin_change():
    coins = [1, 3, 4, 5]
    amount = 7
    result = Solution().coin_change(coins, amount)
    assert result == 2, f"Test for coin change failed. Expected 2, but got {result}"
    print("Test for coin change with bottom up dp approach executed successfully!!!")
    result = Solution2().coin_change(coins, amount)
    assert result == 2, f"Test for coin change failed. Expected 2, but got {result}"
    print("Test for coin change with top bottom dp approach executed successfully!!!")


if __name__ == "__main__":
    test_coin_change()
