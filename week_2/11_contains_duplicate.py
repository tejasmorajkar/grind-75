# https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


def test_contains_duplicate():
    nums = [1,2,3,1]
    result = Solution().contains_duplicate(nums)
    assert result == True