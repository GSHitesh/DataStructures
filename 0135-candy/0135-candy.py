class Solution:
    def candy(self, ratings: List[int]) -> int:
        size = len(ratings)
        if size <= 1:
            return size

        candies = [1]*size

        for i in range(1,size):
            if ratings[i] > ratings[i-1]:
                #Comparing alternative indexes from forward
                candies[i] = candies[i-1] + 1 
        for i in range(size-1,0,-1):
            if ratings[i-1] > ratings[i]:
                #Comparing alternative indexes from backwards
                candies[i-1] = max(candies[i]+1,candies[i-1])
        sum = 0
        for i in range(0,size):
            sum += candies[i]

        return sum
        