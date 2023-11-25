class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        a = strs[0]
        b = strs[-1]
        
        ans = ''
        
        for i in range(0,len(a)):
            if a[i] == b[i]:
                ans += a[i]
            else:
                break
        return ans
        