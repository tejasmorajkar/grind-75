# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def is_palindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        alnum_s = "".join([ch.lower() for ch in s if ch.isalnum()])
        start = 0
        end = len(alnum_s) - 1
        while start < end:
            if alnum_s[start] == alnum_s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True


s = "A man, a plan, a canal: Panama"
print(Solution().is_palindrome(s))