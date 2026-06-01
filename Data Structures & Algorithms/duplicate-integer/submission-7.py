class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hastset = set()
        for num in nums:
            if num in hastset:
                return True
            hastset.add(num)
        return False
         