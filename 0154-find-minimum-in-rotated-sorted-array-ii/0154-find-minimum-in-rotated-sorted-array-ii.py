class Solution:
    def findMin(self, A: List[int]) -> int:
        l,h = 0, len(A)-1
        mid = 0
        while l<h:
            mid = (l+h)//2
            if A[mid] > A[h]:
                l = mid +1
            elif A[mid] < A[l]:
                h= mid
            else:
                h = h-1
        return min(A[l],A[h])
        