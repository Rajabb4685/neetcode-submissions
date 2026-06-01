class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashset 
        # time - o(n)
        # space - o(n)

        # ask hashset if the value already exists, 
        # when interating through it 

        hashset = set() # to store info 

        for n in nums: # look through each value 
            if n in hashset: # if that value is in the hashset
                return True # that means it 'contains duplicate' 
            else: # if not in the hashset
                hashset.add(n) # add to the hashset 
        return False # after iterating through everything, if everything was unique, return false, meaning there is no duplicates 

        
