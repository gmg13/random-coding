from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        count = len(nums)
        # list of all unseen so far
        unseen = set(range(count))
        # max field length
        flen = 0
        # now go through the unknowns and see where we land
        while unseen:
            # get the representive elem
            initial = i = unseen.pop()
            # now to retrieve the list of all field vals for `i`
            seen = set([i])
            while nums[i] not in seen:
                seen.add(nums[i])
                unseen.remove(nums[i])
                i = nums[i]
            # record the max field len
            flen = max(flen, len(seen))
        # return max field length noted
        return flen
