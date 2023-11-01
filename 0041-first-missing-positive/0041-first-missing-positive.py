class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

    # First, move all positive numbers to their correct positions
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Find the first position where nums[i] != i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all numbers from 1 to n are present, return n + 1
        return n + 1