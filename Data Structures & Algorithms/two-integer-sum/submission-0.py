class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevM = {}
        for ind,num in enumerate(nums):
            difference = target - num
            if difference in prevM:
                return [prevM[difference],ind]
            prevM[num]=ind