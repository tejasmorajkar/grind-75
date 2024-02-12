# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List


# Approach to find out rotation first and then binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        rot = low
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            rot_mid = (mid + rot) % len(nums)
            if nums[rot_mid] == target:
                return rot_mid
            elif nums[rot_mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]:
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if target < nums[mid] or target > nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1


def test_search_in_rotated_array():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    actual = Solution2().search(nums, target)
    assert actual == 4, f"Test for search in rotated array failed. Expected 4, but got {actual}"
    nums = [4,5,6,7,0,1,2]
    target = 3
    actual = Solution2().search(nums, target)
    assert actual == -1, f"Test for search in rotated array failed. Expected -1, but got {actual}"
    nums = [1]
    target = 0
    actual = Solution2().search(nums, target)
    assert actual == -1, f"Test for search in rotated array failed. Expected -1, but got {actual}"
    print("Test for search in rotated array executed successfully!!!")


if __name__ == "__main__":
    test_search_in_rotated_array()
