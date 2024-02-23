# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    """Considering each element(odd) and adjacent 2 elements(even) in input as axis and
    checking left and right bounds for palindrome"""
    def longestPalindrome(self, s: str) -> str:
        res_left, res_right, res_len = 0, 0, 0

        for idx in range(len(s)):
            # Odd length palindrome
            curr_left, curr_right = idx, idx
            while curr_left >= 0 and curr_right < len(s) and s[curr_left] == s[curr_right]:
                if (curr_right - curr_left + 1) > res_len:
                    res_left = curr_left
                    res_right = curr_right
                    res_len = res_right - res_left + 1
                curr_left -= 1
                curr_right += 1

            # Even length palindrome
            curr_left, curr_right = idx, idx + 1
            while curr_left >= 0 and curr_right < len(s) and s[curr_left] == s[curr_right]:
                if (curr_right - curr_left + 1) > res_len:
                    res_left = curr_left
                    res_right = curr_right
                    res_len = res_right - res_left + 1
                curr_left -= 1
                curr_right += 1
        return s[res_left:res_right + 1]


class Solution2:
    """Using a dp array to store palindrome with len 1 to n and starting at each index in string
    String with len 1 are palindrome by default
    String with len 2 are palindrome if start and end characters match
    String with bigger length are palindrome if start and end characters match and
    dp[start + 1][end - 1] i.e. is palindrome until previous characters"""
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        palin_start, palin_end = 0, 0
        for gap in range(n):
            start, end = 0, gap
            while start < n and end < n:
                if gap == 0:
                    dp[start][end] = True
                    palin_start, palin_end = start, end
                elif gap == 1 and s[start] == s[end]:
                    dp[start][end] = True
                    palin_start, palin_end = start, end
                elif s[start] == s[end] and dp[start + 1][end - 1]:
                    dp[start][end] = True
                    palin_start, palin_end = start, end
                start += 1
                end += 1
        return s[palin_start: palin_end + 1]


class Solution3:
    """Using Manacher's algorithm"""

    def build_str(self, s: str) -> str:
        """Build a string such it starts with @ and ends with $
        Also separate each char in s by # to allow checking of even length palindromes"""
        updated_s = "@"
        for ch in s:
            updated_s += "#"
            updated_s += ch
        updated_s += "#"
        updated_s += "$"
        return updated_s

    def longestPalindrome(self, s: str):
        updated_s = self.build_str(s)
        n = len(updated_s)
        lps = [0] * n
        center_idx, right_bound_idx = 0, 0

        for idx in range(1, n - 1):
            mirror_idx = center_idx - (idx - center_idx)
            if idx < right_bound_idx:
                lps[idx] = min(lps[mirror_idx], right_bound_idx - idx)

            while updated_s[idx + lps[idx] + 1] == updated_s[idx - lps[idx] - 1]:
                lps[idx] += 1

            if idx + lps[idx] > right_bound_idx:
                center_idx = idx
                right_bound_idx = idx + lps[idx]

        max_len, max_idx = 0, 0
        for idx, ele in enumerate(lps):
            if lps[idx] > max_len:
                max_len = lps[idx]
                max_idx = idx

        first_idx = max_idx - max_len + 1
        actual_first_idx = (first_idx - 2) // 2
        return s[actual_first_idx: actual_first_idx + max_len]


def test_longest_palindrome_substring():
    s = "cbbd"
    result = Solution3().longestPalindrome(s)
    assert result == "bb"
    s = "babad"
    result = Solution3().longestPalindrome(s)
    assert result in ["bab", "aba"]
    s = "a"
    result = Solution3().longestPalindrome(s)
    assert result == "a"
    print("Test for longest palindrome substring executed successfully!!!")


if __name__ == "__main__":
    test_longest_palindrome_substring()
