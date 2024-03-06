# https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key: int, value: int):
        self.key, self.value = key, value
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(-1, -1), Node(-1, -1)
        self.left.next, self.right.prev = self.right, self.left

    def insert(self, node: Node):
        if len(self.cache) == self.capacity:
            self.remove(self.left.next)
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt
        self.cache[node.key] = node

    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        del self.cache[node.key]

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            new_node = Node(node.key, node.value)
            self.insert(new_node)
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        new_node = Node(key, value)
        self.insert(new_node)


def test_lru_cache():
    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    result = obj.get(1)
    assert result == 1
    obj.put(3, 3)
    result = obj.get(2)
    assert result == -1
    obj.put(4, 4)
    result = obj.get(1)
    assert result == -1
    result = obj.get(3)
    assert result == 3
    result = obj.get(4)
    assert result == 4
    print("Tests for LRU Cache executed successfully!!!")


if __name__ == "__main__":
    test_lru_cache()
