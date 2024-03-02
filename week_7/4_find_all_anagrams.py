# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq = [0] * 26
        for ch in p:
            freq[ord(ch) - ord('a')] += 1
        window_freq = [0] * 26
        result = []
        for idx in range(len(s)):
            window_freq[ord(s[idx]) - ord('a')] += 1
            if idx - len(p) >= 0:
                window_freq[ord(s[idx - len(p)]) - ord('a')] -= 1
            if window_freq == freq:
                result.append(idx - len(p) + 1)
        return result
