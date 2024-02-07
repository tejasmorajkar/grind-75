# https://leetcode.com/problems/product-of-array-except-self/
from typing import List


class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        n = len(nums)
        curr = 1
        result = [1] * n
        for idx in range(0, n):
            result[idx] *= curr
            curr *= nums[idx]
        curr = 1
        for idx in range(n - 1, -1, -1):
            result[idx] *= curr
            curr *= nums[idx]
        return result


def test_product_except_self():
    nums = [1, 2, 3, 4]
    actual = Solution().product_except_self(nums)
    assert actual == [24, 12, 8, 6], f"Test for product except self failed. Expected [24, 12, 8, 6] but got {actual}"
    print("Test for product of array except self passed !!!")


if __name__ == "__main__":
    test_product_except_self()
