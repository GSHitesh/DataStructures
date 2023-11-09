class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        if len(s) == 1:
            return 1
        length = 0

        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                length += 1
            else:
                break
        return length
        