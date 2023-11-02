class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <=2:
            return 0
        i=1
        j = len(height)-1
        sum = 0

        l = height[0]
        r= height[-1]
        while i<=j:
            if height[i] > l:
                l = height[i]
            if height[j]> r:
                r = height[j]

            if l<=r:
                sum += l - height[i]
                i=i+1
            else:
                sum += r-height[j]
                j=j-1
        return sum

