# https://leetcode.com/problems/trapping-rain-water/description/
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        ans = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                ans += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                ans += right_max - height[r]

        return ans


height = [0,1,0,2,1,0,1,3,2,1,2,1]
ans = Solution().trap(height)
assert ans == 6