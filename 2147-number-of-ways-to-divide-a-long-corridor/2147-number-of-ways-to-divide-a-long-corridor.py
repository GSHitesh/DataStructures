class Solution(object):
    def numberOfWays(self, corridor):
        res = 1
        seats, aux = 0, 1
        foundSeats = 0

        i = 0; j = 0

        while (i < len(corridor) or j < len(corridor)):
            if ( j < len(corridor) and seats == 2 and corridor[j] != 'S'): j += 1
            elif (seats == 2):

                if (i == j): res *= aux; aux = 1; seats = 0
                else: aux += 1; i += 1

            else:
                if (j == len(corridor)): break
                if (corridor[j] == 'S'): seats += 1; foundSeats += 1
                if (seats == 2): i = j+1

                j += 1
            


        return (res) % (10**9 + 7) if foundSeats >= 2 and foundSeats % 2 == 0 else 0