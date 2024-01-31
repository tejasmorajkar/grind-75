# https://leetcode.com/problems/k-closest-points-to-origin/

from typing import List


class Solution:
    def k_closest(self, points: List[List[int]], k: int) -> List[List[int]]:
        from heapq import heappush, heappop
        dist = []
        for idx in range(len(points)):
            heappush(dist, (points[idx][0] ** 2 + points[idx][1] ** 2, points[idx]))
        result = []
        while k:
            _, points = heappop(dist)
            result.append(points)
            k -= 1
        return result


def test_k_closest_points():
    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    result = Solution().k_closest(points=points, k=k)
    assert result == [[3, 3], [-2, 4]]


if __name__ == "__main__":
    test_k_closest_points()
