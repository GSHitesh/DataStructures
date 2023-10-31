class Solution:
    def nextPermutation(self, nums):
        l = len(nums)
        breakpoint = -1

        for i in range(l - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                breakpoint = i - 1
                break

        if breakpoint < 0:
            # If breakpoint is not found, reverse the entire list
            nums.reverse()
            return

        for i in range(l - 1, -1, -1):
            if nums[breakpoint] < nums[i]:
                nums[breakpoint], nums[i] = nums[i], nums[breakpoint]
                nums[breakpoint + 1:] = nums[breakpoint + 1:][::-1]
                break
