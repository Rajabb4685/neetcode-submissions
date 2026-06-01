class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if not lengths are not the same directly return false 
        if len(s) != len(t):
            return False

        if sorted(s) == sorted(t): # after sorted check they are the same 
            return True 
        return False
        