# https://leetcode.com/problems/01-matrix/description/

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        for idx in range(len(intervals)):
            if newInterval[1] < intervals[idx][0]:
                output.append(newInterval)
                output.extend(intervals[idx:])
                return output
            elif intervals[idx][1] < newInterval[0]:
                output.append(intervals[idx])
            else:
                newInterval = [
                    min(intervals[idx][0], newInterval[0]),
                    max(intervals[idx][1], newInterval[1])
                ]
        output.append(newInterval)
        return output


def test_insert_interval():
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    result = Solution().insert(intervals=intervals, newInterval=newInterval)
    print(result)


if __name__ == "__main__":
    test_insert_interval()
    