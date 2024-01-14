from typing import List
import math


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = math.floor((low + high) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1


numbers = [-1, 0, 3, 5, 9, 12]
target = 9
result = Solution().search(nums=numbers, target=target)
print(result)

numbers = [5]
target = 5
result = Solution().search(nums=numbers, target=target)

print(result)

