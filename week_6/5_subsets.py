# https://leetcode.com/problems/subsets/description/
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def helper(idx: int, curr: List[int]):
            result.append(curr)

            for idx in range(idx, n):
                curr.append(nums[idx])
                helper(idx + 1, curr.copy())
                curr.pop()

        helper(0, [])
        return result


def test_subsets():
    nums = [1, 2, 3]
    result = Solution().subsets(nums)
    print(result)
    nums = [0]
    result = Solution().subsets(nums)
    print(result)


if __name__ == "__main__":
    test_subsets()
