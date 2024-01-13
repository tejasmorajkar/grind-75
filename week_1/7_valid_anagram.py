# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq = dict()
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        for ch in t:
            if ch not in freq or freq[ch] == 0:
                return False
            freq[ch] = freq[ch] - 1
        return all(value == 0 for value in freq.values())


print(Solution().is_anagram(s="anagram", t="nagaram"))
print(Solution().is_anagram(s="rat", t="car"))
