from typing import List


class Solution:
    def threeSum_(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        hashMap = {nums[i]: i for i in range(n)}
        i = 0
        while i < n:
            if nums[i] > 0:
                break
            j = i + 1
            while j < n:
                target = -(nums[i] + nums[j])
                if target in hashMap and hashMap[target] > j:
                    res.append([nums[i], nums[j], target])
                j = hashMap[nums[j]]  # sets j to the last occuring index of nums[j]
                j += 1
            i = hashMap[nums[i]]  # sets i to the last occuring index of nums[i]
            i += 1
        return res


sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
