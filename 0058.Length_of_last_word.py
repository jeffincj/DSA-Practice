class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        words = s.split()
        if not words:
            return 0
        return len(words[-1])
