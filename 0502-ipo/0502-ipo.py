class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        proj = list(zip(capital, profits))
        proj.sort()
        length = len(proj)
        q = []
        ptr = 0

        for i in range(k):
            while ptr < length and w >= proj[ptr][0]:
                heapq.heappush(q, -1 * proj[ptr][1])
                ptr += 1

            if not q:
                break
                
            w += -1 * heapq.heappop(q)

        return w