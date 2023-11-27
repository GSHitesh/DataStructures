class Solution:
    def knightDialer(self, n: int) -> int:
        neighbors=[[4,6],[6,8],[7,9],[4,8],[0,3,9],[],[0,1,7],[2,6],[1,3],[2,4]]
        combs=[1]*10
        for i in range(n-1):
            res=[0]*10
            for j in range(len(combs)):
                for n in neighbors[j]:
                    res[j]+=combs[n]
            combs=res
        return sum(combs)%(10**9+7)