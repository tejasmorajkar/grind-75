# https://leetcode.com/problems/sort-colors/description/
from typing import List


class Solution:
    def swap(self, nums: List[int], i: int, j: int) -> None:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        idx = 0
        while idx <= right:
            if nums[idx] == 0:
                self.swap(nums, idx, left)
                left += 1
            elif nums[idx] == 2:
                self.swap(nums, idx, right)
                right -= 1
                idx -= 1
            idx += 1


def test_sort_colors():
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2], f"Test for sort colors failed." \
                                       f"Expected [0,0,1,1,2,2] but got {nums}"
    print("Test for sort colors executed successfully!!!")


if __name__ == "__main__":
    test_sort_colors()
