# https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)


def test_contains_duplicate():
    nums = [1,2,3,1]
    result = Solution().containsDuplicate(nums)
    assert result == True