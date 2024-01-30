# https://leetcode.com/problems/01-matrix/÷

from typing import List


class Solution:
    DIRECTIONS = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
    ]

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque
        queue = deque()
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1
        while queue:
            r, c = queue.popleft()
            for dr, dc in self.DIRECTIONS:
                new_r, new_c = r + dr, c + dc
                if 0 <= new_r < len(mat) and 0 <= new_c < len(mat[0]) and mat[new_r][new_c] == -1:
                    mat[new_r][new_c] = mat[r][c] + 1
                    queue.append((new_r, new_c))
        return mat


def test_nearest_zero():
    mat = [[0,0,0],[0,1,0],[1,1,1]]
    result = Solution().updateMatrix(mat)
    print(result)


if __name__ == "__main__":
    test_nearest_zero()
