# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invert(self, root: Optional[TreeNode]):
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invert(root.left)
        self.invert(root.right)
        return root

    def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invert(root)


def print_inorder_traversal(root):
    if not root:
        return
    print(root.val)
    print_inorder_traversal(root.left)
    print_inorder_traversal(root.right)


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
result = Solution().invert_tree(root=root)
print_inorder_traversal(result)
