from typing import List


class Solution:
    DIRECTIONS = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]

    def _dfs(self, grid: List[List[str]], row: int, col: int, count: int):
        grid[row][col] = '*'
        for drow, dcol in self.DIRECTIONS:
            new_row = row + drow
            new_col = col + dcol
            if 0 <= new_row < len(grid) and \
                    0 <= new_col < len(grid[0]) and \
                    grid[new_row][new_col] == '1':
                self._dfs(grid, new_row, new_col, count)

    def num_islands(self, grid: List[List[str]]) -> int:
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    self._dfs(grid, row, col, count)
        return count


def test_num_islands():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    actual = Solution().num_islands(grid)
    assert actual == 1, f"Test for num of islands failed. Expected 1, but got {actual}"
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    actual = Solution().num_islands(grid)
    assert actual == 3, f"Test for num of islands failed. Expected 3, but got {actual}"
    print("Test for num of islands executed successfully!!!")


if __name__ == "__main__":
    test_num_islands()
