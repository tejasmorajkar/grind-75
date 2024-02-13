from typing import List


class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def helper(index: int, curr: List[int], total: int):
            if total == target:
                result.append(curr.copy())
                return
            if index == len(candidates) or total > target:
                return
            curr.append(candidates[index])
            helper(index, curr, total + candidates[index])
            curr.pop()
            helper(index + 1, curr, total)

        helper(0, [], 0)
        return result


def test_combination_sum():
    candidates = [2, 3, 6, 7]
    target = 7
    actual = Solution().combination_sum(candidates, target)
    assert actual == [[2, 2, 3], [7]], f"Test for combination sum failed. Expected [[2,2,3], [7]], but got {actual}"
    candidates = [2, 3, 5]
    target = 8
    actual = Solution().combination_sum(candidates, target)
    assert actual == [[2, 2, 2, 2], [2, 3, 3], [3, 5]], (f"Test for combination sum failed. "
                                                         f"Expected [[2,2,2,2],[2,3,3],[3,5]], but got {actual}")
    candidates = [2]
    target = 1
    actual = Solution().combination_sum(candidates, target)
    assert actual == [], f"Test for combination sum failed. Expected [], but got {actual}"
    print("Test for combination sum executed successfully!!!")


if __name__ == "__main__":
    test_combination_sum()
