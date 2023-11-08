class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n<4:
            return []
        
        arr = set()

        nums.sort()

        for i in range(n):
            for j in range(i+1,n):
                left = j+1
                right = n-1
                while left < right:
                    if nums[i]+nums[j]+nums[left]+nums[right] > target:
                        right = right -1
                    elif nums[i]+nums[j]+nums[left]+nums[right] < target:
                        left = left +1
                    else:
                        arr.add((nums[i],nums[j],nums[left],nums[right]))
                        left = left +1
                        right = right-1

        return arr

        