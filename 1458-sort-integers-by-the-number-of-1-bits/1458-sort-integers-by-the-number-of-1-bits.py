class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_ones(n):
            count = 0
            while n:
                n &= (n - 1)  # Clear the least significant 1-bit
                count += 1
            return count

        # Sort the array based on two criteria: the number of 1's and the integer value
        arr.sort(key=lambda x: (count_ones(x), x))

        return arr