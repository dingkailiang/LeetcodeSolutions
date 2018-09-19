METHOD = "twoSum"

TESTCASES = [
    ([2,7,11,15],9),
    ([-1,-2,-3,-4,-5],-8)
]

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mem = {}
        for i in range(len(nums)):
            x = nums[i]
            y = target - x
            if y in mem:
                return [i,mem[y]]
            mem[x] = i