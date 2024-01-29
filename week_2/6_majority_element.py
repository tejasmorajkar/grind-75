# https://leetcode.com/problems/majority-element/
from typing import List


class Solution:
    def majority_element(self, nums: List[int]) -> int:
        count = 0
        candidate = -1
        for num in nums:
            if count == 0:
                candidate = num
            if candidate == num:
                count += 1
            else:
                count -= 1
        return candidate


def test_majority_element():
    nums = [2, 2, 1, 1, 1, 2, 2]
    result = Solution().majority_element(nums)
    print(result)


if __name__ == "__main__":
    test_majority_element()
