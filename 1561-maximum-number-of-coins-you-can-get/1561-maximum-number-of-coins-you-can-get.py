class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        ret = 0
        count = 0
        i = len(piles) - 2
        num_piles = len(piles) // 3
        
        while count < num_piles:
            ret += piles[i]
            i -= 2
            count += 1

        return ret