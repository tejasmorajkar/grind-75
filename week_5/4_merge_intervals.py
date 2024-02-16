# https://leetcode.com/problems/merge-intervals/description/
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        s, e = intervals[0]
        intervals.sort(key=lambda t: t[0])
        s, e = intervals[0]
        for start, end in intervals:
            if e >= start:
                s, e = min(s, start), max(e, end)
            else:
                result.append([s,e])
                s, e = start, end
        result.append([s,e])
        return result
            

def test_merge_intervals():
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    actual = Solution().merge(intervals)
    assert actual == [[1,6],[8,10],[15,18]], f"Test for merge intervals failed." \
    f"Expected [[1,6],[8,10],[15,18]], but got {actual}"
    print("Test for merge intervals executed successfully!!!")


if __name__ == "__main__":
    test_merge_intervals()
