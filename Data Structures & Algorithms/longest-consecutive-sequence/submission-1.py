class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # edge case
        if not nums:
            return 0

        ordered_unique_nums = sorted(set(nums)) # [2,20,4,10,3,4,5] -> [2,20,4,10,3,5] -> [2, 3, 4, 5, 10, 20]

        current_high = 1
        best = 1

        for i in range(1, len(ordered_unique_nums)):
            if ordered_unique_nums[i] - ordered_unique_nums[i - 1] == 1:
                current_high += 1
            else:
                current_high = 1
            best = max(best, current_high)
        
        return best
                
            



        









        