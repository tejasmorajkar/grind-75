# https://leetcode.com/problems/time-based-key-value-store/description/
class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.store.get(key, [])
        low, high = 0, len(values) - 1
        while low <= high:
            mid = (low + high)//2
            mid_timestamp, mid_value = values[mid]
            if mid_timestamp <= timestamp:
                result = mid_value
                low = mid + 1
            else:
                high = mid - 1
        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

def test_time_based_key_value_store():
    obj = TimeMap()
    obj.set("foo", "bar", 1)
    actual = obj.get("foo", 1)
    assert actual == "bar", f"Get operation failed. Expected 'bar', but got {actual}"
    actual = obj.get("foo", 3)
    assert actual == "bar", f"Get operation failed. Expected 'bar', but got {actual}"
    obj.set("foo", "bar2", 4)
    actual = obj.get("foo", 4)
    assert actual == "bar2", f"Get operation failed. Expected 'bar2', but got {actual}"
    actual = obj.get("foo", 5)
    assert actual == "bar2", f"Get operation failed. Expected 'bar2', but got {actual}"
    print("Test for time based key value store executed successfully!!!")


if __name__ == "__main__":
    test_time_based_key_value_store()
