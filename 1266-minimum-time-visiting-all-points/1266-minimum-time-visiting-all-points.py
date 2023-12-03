class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(1,len(points)):
            for j in range(1,len(points[0])):
                res_curr = max(abs(points[i-1][j-1]-points[i][j-1]), abs(points[i-1][j]-points[i][j]))
                res += res_curr
        return res
        