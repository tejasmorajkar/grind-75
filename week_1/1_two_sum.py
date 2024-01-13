# https://leetcode.com/problems/two-sum/description/

from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = dict()
        result = []
        for idx, num in enumerate(nums):
            if (target - num) in num_to_index:
                result.extend([idx, num_to_index[target - num]])
                break
            num_to_index[num] = idx
        return result


print(Solution().two_sum(nums=[2, 7, 11, 15], target=9))
