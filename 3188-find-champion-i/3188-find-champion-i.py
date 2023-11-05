class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        return max(grid).index(0)
        