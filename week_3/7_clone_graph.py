# https://leetcode.com/problems/clone-graph/description/
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def __init__(self):
        self.original_to_clone = {}

    def _dfs(self, node: Optional['Node']) -> Optional['Node']:
        if node in self.original_to_clone:
            return self.original_to_clone[node]

        clone_node = Node(node.val)
        self.original_to_clone[node] = clone_node

        for neigh in node.neighbors:
            clone_node.neighbors.append(self._dfs(neigh))
        return clone_node

    def clone_graph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        return self._dfs(node)


def test_clone_graph():
    one, two, three, four = Node(1), Node(2), Node(3), Node(4)
    one.neighbors.extend((two, four))
    two.neighbors.extend((one, three))
    three.neighbors.extend((two, four))
    four.neighbors.extend((one, three))
    result = Solution().clone_graph(one)
    print(result)


if __name__ == "__main__":
    test_clone_graph()
