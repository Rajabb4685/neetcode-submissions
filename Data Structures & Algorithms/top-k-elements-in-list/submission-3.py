class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Given an integer array {nums} and an integer {k}, return the the  frequent elements
        # with in the array

        # I would need to find the count of times each time shows up (frequence)
        # run through the loop of array with in the count, and return amount in each bucket

        # i -> the bucket  

        count = {}
        freq = [[]for i in range(len(nums) + 1)]

        # go through every value in nums, and count how manu time each of them shows up
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n,c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res



