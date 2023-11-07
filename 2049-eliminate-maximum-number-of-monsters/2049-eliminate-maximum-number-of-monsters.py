class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival_time = [(dist[i]-1)//speed[i]+1 for i in range(len(dist))]

        monsters = list(zip(arrival_time,range(len(dist))))
        monsters.sort()
        time,eliminated = 0,0

        for arrival_time, monster in monsters:
            if time < arrival_time:
                eliminated = eliminated +1
                time = time+1
            else:
                break
        return eliminated


        