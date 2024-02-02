# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        char_map = [-1] * 128
        for right in range(len(s)):
            if char_map[ord(s[right])] >= left:
                left = char_map[ord(s[right])] + 1
            char_map[ord(s[right])] = right
            longest = max(longest, right - left + 1)
        return longest