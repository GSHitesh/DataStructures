class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        count = [0] * (length + 1)

        for num in nums:
            count[num] += 1
            if count[num] > 1:
                return num

        return length
