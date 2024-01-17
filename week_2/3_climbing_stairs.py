class Solution:
    def climbStairs(self, n: int) -> int:
        curr, prev = 1, 1
        for i in range(n - 1):
            temp = curr
            curr = curr + prev
            prev = temp
        return curr
        
def test_climb_stairs():
    sol1 = Solution()
    n = 3
    actual_result = sol1.climbStairs(n)
    assert actual_result == 3, f"Test failed !!! Expected 3 but got {actual_result}"

    n = 5
    actual_result = sol1.climbStairs(n)
    assert actual_result == 8, f"Test failed !!! Expected 8 but got {actual_result}"