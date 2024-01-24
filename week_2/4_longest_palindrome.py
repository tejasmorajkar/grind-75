# https://leetcode.com/problems/longest-palindrome/description/

class Solution:
    def longest_palindrome(self, s: str) -> int:
        odd_count = 0
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
            if freq[ch] % 2 == 0:
                odd_count -= 1
            else:
                odd_count += 1
        if odd_count > 1:
            return len(s) - odd_count + 1
        return len(s)


s = "abccccdd"
print(Solution().longest_palindrome(s))