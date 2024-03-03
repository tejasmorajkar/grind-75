# https://leetcode.com/problems/task-scheduler/
import heapq
from collections import Counter, deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_heap = [-c for c in freq.values()]
        heapq.heapify(max_heap)
        q = deque()
        time = 0

        while max_heap or q:
            time += 1
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap)
                if cnt:
                    q.append((cnt, time + n))
            if q and q[0][1] == time:
                c, _ = q.popleft()
                heapq.heappush(max_heap, c)
        return time


def test_task_scheduler():
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    time = Solution().leastInterval(tasks, n)
    assert time == 8
    tasks = ["A", "C", "A", "B", "D", "B"]
    n = 1
    time = Solution().leastInterval(tasks, n)
    assert time == 6
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 3
    time = Solution().leastInterval(tasks, n)
    assert time == 10
    print("Test for task scheduler executed successfully!!!")


if __name__ == "__main__":
    test_task_scheduler()
