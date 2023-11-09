class Solution:
    def maxPower(self, s: str) -> int:

        maxi = 1
        current_max = 1

        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                current_max += 1
            else:
                current_max = 1
            if current_max > maxi:
                maxi = current_max
        return maxi
        