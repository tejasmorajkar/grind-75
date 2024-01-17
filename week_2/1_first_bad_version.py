# https://leetcode.com/problems/first-bad-version/description/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        while low <= high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                high = mid - 1
            else:
                low = mid + 1
        return high
        