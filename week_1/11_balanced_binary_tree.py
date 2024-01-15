# https://leetcode.com/problems/balanced-binary-tree/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = True

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.dfs(root.left)
        right_height = self.dfs(root.right)
        if abs(left_height - right_height) > 1:
            self.result = False
        height = max(left_height, right_height) + 1
        return height


    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        return self.result


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
sol1 = Solution()
sol1.is_balanced(root)
print(sol1.result)

root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
sol2 = Solution()
sol2.is_balanced(root)
print(sol2.result)