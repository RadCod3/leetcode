from typing import List


class Solution:
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     n = len(nums1)
    #     m = len(nums2)

    #     merged = []
    #     mid = (m + n) // 2
    #     i = j = 0
    #     while i < n and j < m and i + j < mid + 1:
    #         if nums1[i] < nums2[j]:
    #             merged.append(nums1[i])
    #             i += 1
    #         else:
    #             merged.append(nums2[j])
    #             j += 1

    #     # leftovers num1
    #     if i < n and i + j < mid + 1:
    #         merged = merged + nums1[i:]
    #     # leftovers num2
    #     elif j < m and i + j < mid + 1:
    #         merged = merged + nums2[j:]

    #     if (m + n) % 2 == 0:
    #         return (merged[mid - 1] + merged[mid]) / 2
    #     else:
    #         return merged[mid]

    # Binary Search approach https://www.youtube.com/watch?v=q6IEA26hvXc
    # When finding the median of an array we partition the array into two parts and get the middle.
    # Since the arrays are sorted we can use binary search when adjusting the partition.
    # So lets say we need more elements from A, instead of adding elements to A one by one we do it using binary search.
    # Which ends up giving us a solution of O(log(min(m,n)))
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            mid_a = (l + r) // 2
            mid_b = half - mid_a - 2

            Aleft = A[mid_a] if mid_a >= 0 else float("-inf")
            Aright = A[mid_a + 1] if mid_a + 1 < len(A) else float("inf")
            Bleft = B[mid_b] if mid_b >= 0 else float("-inf")
            Bright = B[mid_b + 1] if mid_b + 1 < len(B) else float("inf")

            # if partition correct
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = mid_a - 1
            else:
                l = mid_a + 1


sol = Solution()
nums1 = [1, 2, 4, 5, 6, 8, 10, 13, 15, 17, 18]
nums2 = [1, 2, 6, 10, 11, 12, 13, 14, 14, 14, 15, 16]
print(sol.findMedianSortedArrays(nums1, nums2))
