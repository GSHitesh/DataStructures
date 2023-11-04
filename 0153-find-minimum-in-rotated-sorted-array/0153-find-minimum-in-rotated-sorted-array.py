class Solution:
    def findMin(self, A):
        l = 0
        h = len(A) - 1
        
        while l < h:
            mid = (l + h) // 2
            if A[mid] > A[h]:
                l = mid+1
            else:
                h = mid
                
        return A[l]
