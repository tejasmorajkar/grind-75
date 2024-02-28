# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_to_letter = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        n = len(digits)
        result = []
        if not n:
            return result

        def helper(idx: int, curr):
            if idx == n:
                result.append(curr)
                return
            letters = number_to_letter.get(digits[idx], "")
            for letter in letters:
                helper(idx + 1, curr + letter)

        helper(0, "")
        return result
