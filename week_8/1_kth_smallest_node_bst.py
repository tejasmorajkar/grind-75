# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, node: Optional[TreeNode], result: List[int]):
        if node is None:
            return
        self.inorder(node.left, result)
        result.append(node.val)
        self.inorder(node.right, result)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        self.inorder(root, result)
        return result[k - 1]


def test_kth_smallest_node_bst():
    # root = [5, 3, 6, 2, 4, null, null, 1]
    root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    result = Solution().kthSmallest(root, 3)
    assert result == 3
    print("Test for kth smallest node executed successfully!!!")


if __name__ == "__main__":
    test_kth_smallest_node_bst()
