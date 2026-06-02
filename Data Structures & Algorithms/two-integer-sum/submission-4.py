class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force 
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i,j]

        # hash map 

        prevmap = {}

        for i, n in enumerate(nums):
            diff = target - n # simple, by only looking for one value 
            if diff in prevmap: # if the diff, we're looking to make our two sum, is found 
                return [prevmap[diff], i]
            else: 
                prevmap[n] = i # if the value doesn't exist (i.e, the diff isn't found, add the value to the list, since, there is solution, we will see it along the lines, and two values will match)
        
        # return []


