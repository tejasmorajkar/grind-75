from typing import List
import math

class Solution:
    def max_subarray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        curr_sum = 0
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
        return max_sum


def test_max_subarray():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = Solution().max_subarray(nums)
    assert result == 6, f"Test for max sub array failed. Expected 6, but got {result}"
    nums = [5, 4, -1, 7, 8]
    result = Solution().max_subarray(nums)
    assert result == 23, f"Test for max sub array failed. Expected 23, but got {result}"
    print("Test for max subarray sum executed successfully!!!")


if __name__ == "__main__":
    test_max_subarray()
