# https://leetcode.com/problems/word-break/description/
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def build_trie(self, wordDict: List[str], curr: TrieNode):
        for word in wordDict:
            for ch in word:
                if ch not in curr.children:
                    curr.children[ch] = TrieNode()
                curr = curr.children[ch]
            curr.end_of_word = True
            curr = self.root

    def dfs(self, idx: int, n: int, s: str, curr: TrieNode) -> bool:
        if idx == n:
            return curr.end_of_word
        if s[idx] not in curr.children:
            return False
        curr = curr.children[s[idx]]
        if curr.end_of_word:
            old_curr = curr
            curr = self.root
            return self.dfs(idx + 1, n, s, curr) or \
                self.dfs(idx + 1, n, s, old_curr)
        return self.dfs(idx + 1, n, s, curr)

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        self.build_trie(wordDict, self.root)
        return self.dfs(0, n, s, self.root)


class SolutionDP:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True
        for idx in range(n - 1, -1, -1):
            for word in wordDict:
                word_len = len(word)
                if (idx + word_len) <= n and s[idx: idx + word_len] == word:
                    dp[idx] = dp[idx + word_len]
                if dp[idx]:
                    break
        return dp[0]


def test_word_break():
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    actual = Solution().wordBreak(s, wordDict)
    assert not actual
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    actual = Solution().wordBreak(s, wordDict)
    assert actual
    print("Test for word break executed successfully!!!")


def test_word_break_using_dp():
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    actual = SolutionDP().wordBreak(s, wordDict)
    assert not actual
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    actual = SolutionDP().wordBreak(s, wordDict)
    assert actual
    print("Test for word break executed successfully!!!")



if __name__ == "__main__":
    test_word_break()
    test_word_break_using_dp()
