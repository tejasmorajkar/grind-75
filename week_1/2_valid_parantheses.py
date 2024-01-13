# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    MATCHING_PARANTHESES = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    def is_valid(self, s: str) -> bool:
        from queue import LifoQueue
        st = LifoQueue()
        for ch in s:
            if ch in self.MATCHING_PARANTHESES.keys():
                st.put(ch)
            elif st.empty() or not self.MATCHING_PARANTHESES[st.get()] == ch:
                return False
        return st.empty()


print(Solution().is_valid("()[]{}"))