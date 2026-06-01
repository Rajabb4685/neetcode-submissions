class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 3. Sorting

        # sorted() function, which takes an iterable (like a string) 
        # and returns a sorted list of its characters.

        # Time complexity: o(n log n)
        # Space complexity: o(n)
        

        # if sorted(s) == sorted(t):
        #     return True
        # return False
        if len(s) != len(t):
            return False
            
        return sorted(s) == sorted(t)



