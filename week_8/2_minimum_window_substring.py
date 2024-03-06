# https://leetcode.com/problems/minimum-window-substring/
import math


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_window, count_t = {}, {}
        for ch in t:
            count_t[ch] = 1 + count_t.get(ch, 0)
        have, need = 0, len(count_t)
        left = 0
        res, res_len = (-1, -1), math.inf
        for right in range(len(s)):
            right_ch = s[right]
            count_window[right_ch] = 1 + count_window.get(right_ch, 0)
            if right_ch in count_t and count_window[right_ch] == count_t[right_ch]:
                have += 1
            while have == need:
                curr_len = right - left + 1
                if curr_len < res_len:
                    res = (left, right)
                    res_len = curr_len
                left_ch = s[left]
                count_window[left_ch] -= 1
                if left_ch in count_t and count_window[left_ch] < count_t[left_ch]:
                    have -= 1
                left += 1
        left, right = res
        return s[left: right + 1]


def test_minimum_window_substring():
    s = "ADOBECODEBANC"
    t = "ABC"
    result = Solution().minWindow(s, t)
    assert result == "BANC"
    print("Test for minimum window substring executed successfully!!!")


if __name__ == "__main__":
    test_minimum_window_substring()
