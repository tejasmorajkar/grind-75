# https://leetcode.com/problems/add-binary/

class Solution:
    def add_binary(self, a: str, b: str) -> str:
        m = len(a) - 1
        n = len(b) - 1
        result = ""
        carry = 0
        while m >= 0 or n >= 0 or carry > 0:
            sum_result = 0
            if m >= 0:
                sum_result += int(a[m])
            if n >= 0:
                sum_result += int(b[n])
            if carry > 0:
                sum_result += carry
            carry = sum_result // 2
            result = str(sum_result % 2) + result
            m -= 1
            n -= 1
        return result


def test_add_binary():
    a = "100"
    b = "101"
    result = Solution().add_binary(a, b)
    print(result)


if __name__ == "__main__":
    test_add_binary()
