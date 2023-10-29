class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mini, maxi, length = nums.index(min(nums)), nums.index(max(nums)), len(nums)
        # Scenario 1: Both elements are removed by only deleting from the front.
        case1 = max(mini,maxi) + 1

        # Scenario 2: Both elements are removed by only deleting from the back.
        case2 = length - min(mini,maxi)
        
        # Scenario 3: Delete from the front to remove one of the elements, and delete from the    back   to remove the other element.
        left, right = min(mini,maxi), max(mini,maxi)
        case3 = (left + 1) + (length-right)

        #comparing three cases
        return min(case1,case2,case3)
                    

            
        