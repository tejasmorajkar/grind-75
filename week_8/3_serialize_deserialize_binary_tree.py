# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x: int):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def __init__(self):
        self.idx = None

    def preorder(self, node: Optional[TreeNode], traversal):
        if not node:
            traversal.append("N")
            return
        traversal.append(str(node.val))
        self.preorder(node.left, traversal)
        self.preorder(node.right, traversal)

    def serialize(self, root: Optional[TreeNode]):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        traversal = []
        self.preorder(root, traversal)
        return ",".join(traversal)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        self.idx = 0

        def dfs() -> Optional[TreeNode]:
            if data[self.idx] == "N":
                self.idx += 1
                return None
            node = TreeNode(int(data[self.idx]))
            self.idx += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
ans = deser.deserialize(ser.serialize(root))