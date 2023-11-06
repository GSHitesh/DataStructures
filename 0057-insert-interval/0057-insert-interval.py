class Solution:
    def insert(self, intervals: List[List[int]], newIntervals: List[int]) -> List[List[int]]:
        interval = []

        for i in intervals:
            if i[1] < newIntervals[0]:
                interval.append(i)
            elif i[0] > newIntervals[1]:
                interval.append(newIntervals)
                newIntervals = i
            elif i[0] <= newIntervals[1] or i[1] >= newIntervals[0]:
                newIntervals[0] = min(i[0],newIntervals[0])
                newIntervals[1] = max(i[1],newIntervals[1])

        interval.append(newIntervals)
        return interval
        