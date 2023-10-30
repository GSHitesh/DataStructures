class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = float('-inf')
        current_sum = 0
        for i in range(0,len(nums)):
            current_sum += nums[i]
            if(current_sum > max_so_far):
                max_so_far = current_sum
            if current_sum < 0:
                current_sum = 0
        return max_so_far

        