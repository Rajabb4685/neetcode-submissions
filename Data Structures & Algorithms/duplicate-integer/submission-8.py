class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # newNums = sorted(nums)
        # for i in range(1, len(newNums)):
        #     if newNums[i] == newNums[i - 1]:
        #         return True
        # return False

        if len(set(nums)) < len(nums):
            return True 
        return False

        

