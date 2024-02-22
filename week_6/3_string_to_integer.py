# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    @staticmethod
    def myAtoi(s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        result = 0
        negative = None
        for idx in range(len(s)):
            if s[idx] == '-' and idx == 0:
                negative = True
            elif s[idx] == "+" and idx == 0:
                negative = False
            elif s[idx].isdigit():
                digit = int(s[idx])
                result = result * 10 + digit
            else:
                break
        result = result * (-1 if negative else 1)
        if result > (pow(2, 31) - 1):
            result = pow(2, 31) - 1
        elif result < -pow(2, 31):
            result = -pow(2, 31)
        return result


def test_string_to_integer():
    s = "42"
    actual = Solution.myAtoi(s)
    assert actual == 42
    s = "   -42"
    actual = Solution.myAtoi(s)
    assert actual == -42
    s = "4193 with words"
    actual = Solution.myAtoi(s)
    assert actual == 4193
    print("Test for string to integer executed successfully!!!")


if __name__ == "__main__":
    test_string_to_integer()
