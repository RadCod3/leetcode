from typing import List


class Solution:
    def trapOld(self, height: List[int]) -> int:
        n = len(height)
        if n == 1:
            return 0
        leftMax = [0] * n
        rightMax = [0] * n

        for i in range(1, n - 1):
            leftMax[i] = max(leftMax[i - 1], height[i - 1])
            rightMax[n - i - 1] = max(rightMax[n - i], height[n - i])

        leftMax[-1] = max(leftMax[-2], height[-2])
        rightMax[0] = max(rightMax[1], height[1])

        minHeight = [max(min(leftMax[i], rightMax[i]) - height[i], 0) for i in range(n)]
        return sum(minHeight)

    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 2:
            return 0

        maxLeft = height[0]
        maxRight = height[n - 1]
        l, r = 1, n - 2
        val = 0

        while l <= r:
            if maxLeft < maxRight:
                if maxLeft < height[l]:
                    maxLeft = height[l]
                else:
                    val += maxLeft - height[l]
                l += 1
            else:
                if maxRight < height[r]:
                    maxRight = height[r]
                else:
                    val += maxRight - height[r]
                r -= 1

        return val


sol = Solution()
print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(sol.trap([4, 2, 0, 3, 2, 5]))
