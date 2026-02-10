class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}

        for i, num in enumerate(nums):
            res = target - num
            if res in num_map:
                return [num_map[res], i]
            num_map[num] = i