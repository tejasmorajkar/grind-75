# https://leetcode.com/problems/minimum-height-trees/
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = [set() for _ in range(n)]

        for x, y in edges:
            adj[x].add(y)
            adj[y].add(x)

        leaves = [node for node, nei in enumerate(adj) if len(nei) == 1]

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                nei = adj[leaf].pop()
                adj[nei].remove(leaf)
                if len(adj[nei]) == 1:
                    new_leaves.append(nei)
            leaves = new_leaves

        return leaves
