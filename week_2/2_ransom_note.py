# https://leetcode.com/problems/ransom-note/description/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_char_freq = dict()
        for ch in magazine:
            mag_char_freq[ch] = mag_char_freq.get(ch, 0) + 1
        for ch in ransomNote:
            if ch not in mag_char_freq or mag_char_freq[ch] == 0:
                return False
            mag_char_freq[ch] -= 1
        return True


def test_can_construct():
	sol1 = Solution()
	ransomNote = "aa"
	magazine = "aab"
	actual_result = sol1.canConstruct(ransomNote, magazine)
	assert actual_result == True, "Test failed ! Expected 'True' but got 'False'"

	ransomNote = "aa"
	magazine = "ab"
	actual_result = sol1.canConstruct(ransomNote, magazine)
	assert actual_result == False, "Test failed ! Expected 'False' but got 'True'"


if __name__ == "__main__":
	test_can_construct()