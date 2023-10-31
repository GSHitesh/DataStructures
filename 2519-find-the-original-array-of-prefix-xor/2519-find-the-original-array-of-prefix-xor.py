class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # If the input list has only one element, return it as is.
        if len(pref) == 1:
            return pref

        # Initialize the answer list with the first element of pref.
        ans = [pref[0]]

        # Iterate through the elements in pref, starting from the second element.
        for i in range(len(pref) - 1):
            # Calculate the current element in ans by XORing the current element in pref
            # with the next element in pref.
            ans.append(pref[i] ^ pref[i + 1])

        # Return the ans list as the result.
        return ans