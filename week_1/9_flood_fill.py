# https://leetcode.com/problems/flood-fill/
from typing import List


class Solution:
    DIRECTIONS = [
        (-1, 0),  # Top
        (0, 1),  # Right
        (1, 0),  # Bottom
        (0, -1)  # Left
    ]

    def fill(self, image: List[List[int]], x: int, y: int, starting_color: int, new_color: int):
        if image[x][y] == new_color:
            return
        image[x][y] = new_color
        for dx, dy in self.DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(image) and 0 <= new_y < len(image[0]) \
                    and image[new_x][new_y] == starting_color:
                self.fill(image, new_x, new_y, starting_color, new_color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.fill(image, sr, sc, image[sr][sc], color)
        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
Solution().floodFill(image, sr, sc, color)
print(image)

image = [[0, 0, 0], [0, 0, 0]]
sr = 0
sc = 0
color = 0
Solution().floodFill(image, sr, sc, color)
print(image)
