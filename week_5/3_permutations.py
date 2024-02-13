# https://leetcode.com/problems/permutations/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums[:]]
        for _ in range(len(nums)):
            temp = nums.pop(0)
            permutations = self.permute(nums)
            for permutation in permutations:
                permutation.append(temp)
            nums.append(temp)
            result.extend(permutations)
        return result


def test_permutations():
    nums = [1, 2, 3]
    result = Solution().permute(nums)
    assert result == [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]], \
        f"Test for permutations failed." \
        f"Expected [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]], but got {result}"
    print("Test for permutations executed successfully!!!")


if __name__ == "__main__":
    test_permutations()
