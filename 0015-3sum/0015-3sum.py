class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()

        if len(nums) < 3:
            return []

        if nums[0] > 0:
            return []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            low, high = i + 1, len(nums) - 1

            while low < high:
                total = nums[i] + nums[low] + nums[high]

                if total > 0:
                    high -= 1
                elif total < 0:
                    low += 1
                else:
                    result.add((nums[i], nums[low], nums[high]))
                    # while low < high and nums[low] == nums[low + 1]:
                    #     low += 1
                    # while low < high and nums[high] == nums[high - 1]:
                    #     high -= 1
                    low += 1
                    high -= 1

        return list(result)