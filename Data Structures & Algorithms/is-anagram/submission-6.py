class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashmap
# for an anagram, both length should be the same
# if not return false, cause then it won't be a anagram
        if len(s) != len(t): 
            return False

        # create the hashmaps
        # hashmaps, store the amount of times an value shows up
        countS, countT = {}, {}
        # going through the maps, and add each time we see each value
        for i in range(len(s)):
            # when we see a value, add 1 to it 
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            # if the value being not have same amount as in s to t,
            if countS[c] != countT.get(c,0):
                # retun false because they have different value/amount 
                return False 

        # return true if, they have the same characters, and amount, which makes then valid anagrams of each other 
        return True