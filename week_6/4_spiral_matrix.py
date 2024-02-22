# https://leetcode.com/problems/spiral-matrix/description/
from typing import List


class Solution:
    DIRECTIONS = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction_idx = 0
        n, m = len(matrix), len(matrix[0])
        row, col = 0, 0
        result = [matrix[0][0]]
        matrix[0][0] = 101

        while True:
            direction_idx %= 4
            d_row, d_col = self.DIRECTIONS[direction_idx]
            new_row, new_col = row + d_row, col + d_col

            if 0 <= new_row < n and 0 <= new_col < m and matrix[new_row][new_col] != 101:
                row, col = new_row, new_col
                result.append(matrix[row][col])
                matrix[row][col] = 101
            else:
                direction_idx += 1

            if len(result) == n * m:
                break
        return result


def test_spiral_matrix():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = Solution().spiralOrder(matrix)
    assert result == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    result = Solution().spiralOrder(matrix)
    assert result == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    print("Test for spiral matrix executed successfully!!!")


if __name__ == "__main__":
    test_spiral_matrix()
