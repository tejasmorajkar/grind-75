# https://leetcode.com/problems/word-search/
from functools import cache
from typing import List


class Solution:
    def dfs(self, board, word, row, col, idx) -> bool:
        if idx == len(word):
            return True
        if not(0 <= row < len(board)) or not(0 <= col < len(board[0])) or board[row][col] != word[idx]:
            return False
        temp = board[row][col]
        board[row][col] = "#"
        result = self.dfs(board, word, row - 1, col, idx + 1) or self.dfs(board, word, row, col + 1, idx + 1) or self.dfs(board, word, row + 1, col, idx + 1) or self.dfs(board, word, row, col - 1, idx + 1)
        board[row][col] = temp
        return result


    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                return self.dfs(board, word, row, col, 0)
        return False


def test_word_search():
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    result = Solution().exist(board, word)
    assert result


if __name__ == "__main__":
    test_word_search()
