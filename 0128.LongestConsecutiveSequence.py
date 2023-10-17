from typing import List


class Solution:
    # There may be a better solution with union find
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        curr_max = 0
        for num in nums:
            # check if seq starting num
            if num - 1 in nums:
                continue
            loc_max = 0
            while num in nums:
                loc_max += 1
                num += 1
            curr_max = max(loc_max, curr_max)

        return curr_max


sol = Solution()
print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
