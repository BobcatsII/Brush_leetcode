class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        n = len(nums)
        for x in range(n):
            if target - nums[x] in d:
                return d[target - nums[x]], x
            else:
                d[nums[x]] = x
