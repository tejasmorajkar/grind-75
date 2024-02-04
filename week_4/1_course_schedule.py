# https://leetcode.com/problems/course-schedule/
import collections
from typing import List


# DFS approach
class Solution:
    def __init__(self):
        self.visited = set()
        self.pre_requisites = {}

    def _dfs(self, course: int) -> bool:
        if course in self.visited:
            return False
        if not self.pre_requisites[course]:
            return True
        self.visited.add(course)

        for idx, pre in enumerate(self.pre_requisites[course]):
            if not self._dfs(pre):
                return False
            self.pre_requisites[course].pop(idx)
        self.visited.remove(course)
        return True

    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        for i in range(num_courses):
            self.pre_requisites[i] = []
        for course, pre in prerequisites:
            self.pre_requisites[course].append(pre)
        for course in range(num_courses):
            if not self._dfs(course):
                return False
        return True


# Topologic sort using Kahn's algo
class Solution2:
    def can_finish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(num_courses)]
        indegree = [0] * num_courses
        for u, v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1
        queue = collections.deque()
        for i in range(num_courses):
            if indegree[i] == 0:
                queue.append(i)
        visited = 0
        while queue:
            ele = queue.popleft()
            visited += 1

            for nei in adj[ele]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return visited == num_courses
