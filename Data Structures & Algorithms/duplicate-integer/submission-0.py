class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for num in range(1,len(nums)):
            if nums[num-1]==nums[num]:
                return True
        return False