import collections
from typing import List


class Solution:
    DIRECTIONS = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]

    def oranges_rotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh_orange_count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh_orange_count += 1
                elif grid[row][col] == 2:
                    q.append((row, col))
        if fresh_orange_count == 0:
            return 0
        minutes = 0
        while q:
            q_len = len(q)
            for _ in range(q_len):
                row, col = q.popleft()
                for drow, dcol in self.DIRECTIONS:
                    new_row = row + drow
                    new_col = col + dcol
                    if 0 <= new_row < len(grid) and \
                            0 <= new_col < len(grid[0]) and \
                            grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        q.append((new_row, new_col))
                        fresh_orange_count -= 1
            minutes += 1
        return minutes - 1 if fresh_orange_count == 0 else -1


def test_rotting_oranges():
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    actual = Solution().oranges_rotting(grid)
    assert actual == 4, f"Test for rotting oranges failed. Expected 4, but got {actual}"
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    actual = Solution().oranges_rotting(grid)
    assert actual == -1, f"Test for rotting oranges failed. Expected -1, but got {actual}"
    grid = [[0,2]]
    actual = Solution().oranges_rotting(grid)
    assert actual == 0, f"Test for rotting oranges failed. Expected 0, but got {actual}"
    print("Test for rotting oranges executed successfully!!!")


if __name__ == "__main__":
    test_rotting_oranges()
