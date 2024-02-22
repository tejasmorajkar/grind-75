# https://leetcode.com/problems/partition-equal-subset-sum/
from functools import cache
from typing import List


class Solution:
    @staticmethod
    def can_partition(nums: List[int]) -> bool:
        """Bottom up dp approach
        Store all possible sum if we include given num or not"""
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        target = total_sum // 2
        n = len(nums)
        dp = set()
        dp.add(0)
        for idx in range(n):
            new_dp = set()
            for ele in dp:
                curr_sum = ele + nums[idx]
                if curr_sum == target:
                    return True
                new_dp.add(curr_sum)
                new_dp.add(ele)
            dp = new_dp
            print(dp)
        return False


class Solution2:
    @staticmethod
    def can_partition(nums: List[int]) -> bool:
        """Recursive decision-tree approach with backtracking with caching
        n: len(nums)
        Time-complexity: O(2*n)"""
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        target = total_sum // 2

        @cache
        def helper(idx: int, curr_sum: int) -> bool:
            if curr_sum == target:
                return True
            elif idx == len(nums) or curr_sum > target:
                return False
            return helper(idx + 1, curr_sum + nums[idx]) or helper(idx + 1, curr_sum)

        return helper(0, 0)


def test_can_partition():
    nums = [1, 5, 11, 5]
    actual = Solution.can_partition(nums)
    assert actual
    nums = [1, 2, 3, 5]
    actual = Solution.can_partition(nums)
    assert not actual
    nums = [1, 5, 11, 5]
    actual = Solution2.can_partition(nums)
    assert actual
    nums = [1, 2, 3, 5]
    actual = Solution2.can_partition(nums)
    assert not actual
    print("Test for can partition executed successfully")


if __name__ == "__main__":
    test_can_partition()
