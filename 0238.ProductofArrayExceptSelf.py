from typing import List


class Solution:
    # Uses postfix and prefix product arrays to compute the product of all elements except self.
    # Made more efficient by storing answer on result and not maintining postfix prefix arrays.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        temp = 1
        for i in reversed(range(n - 1)):
            temp = temp * nums[i + 1]
            result[i] *= temp

        return result


sol = Solution()
print(sol.productExceptSelf([-1, 1, 0, -3, 3]))
