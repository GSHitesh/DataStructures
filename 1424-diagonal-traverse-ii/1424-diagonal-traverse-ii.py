class Solution(object):
    def findDiagonalOrder(self, nums):
        mp = {}
        n = 0
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                mp.setdefault(i + j, []).append(nums[i][j])
                n = max(n, i + j)
        
        res = []
        for i in range(n + 1):
            if i in mp:
                res.extend(mp[i][::-1])
        return res
