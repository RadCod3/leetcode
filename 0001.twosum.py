from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    i = 0
    j = len(nums) - 1
    nums_ = [[x, id] for id, x in enumerate(nums)]
    nums_.sort(key=lambda x: x[0])
    while nums_[i][0] + nums_[j][0] != target:
        if i == j:
            return [0, 0]
        elif nums_[i][0] + nums_[j][0] > target:
            j -= 1
        elif nums_[i][0] + nums_[j][0] < target:
            i += 1
    i = nums_[i][1]
    j = nums_[j][1]
    return [i, j]


def twoSum2(nums: List[int], target: int) -> List[int]:
    hashMap = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in hashMap:
            return [hashMap[diff], i]
        hashMap[nums[i]] = i


print(twoSum([1, 6142, 8192, 10239], 18431))
