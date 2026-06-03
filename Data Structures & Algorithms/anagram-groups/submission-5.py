class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap
        # if statement should check if the current str in sorted matches the key
        # if not then make a new key, and store the same value in it's original form 

        # give appropriate names for variables and names 
        # hashmap -> anagramGroups

        # anagramGroups = {} # hashmap to store the grouped anagrams 

        # for s in strs:
        #     # b/c sorted return, turns our string into list, for "eat" -> ['a', 'e', 't']
        #     # so we used "".join to join the list into a string again 
        #     sortedS = "".join(sorted(s)) 

        #     if sortedS in anagramGroups:
        #         # we're appending to the list
        #         anagramGroups[sortedS].append(s)
        #     else:
        #         anagramGroups[sortedS] = [s]

        # # we're returning all the values in a list 
        # return list(anagramGroups.values()) # return in a list




        res = defaultdict(list)

        for s in strs: # interate through strs
            count = [0] * 26 # make an array of 26 values of 0
            for c in s: # interate through the s (current value in strs)
                count[ord(c) - ord('a')] += 1 # finding at what position in our array the letter should go alphabetically 
            res[tuple(count)].append(s) # we use tuple because list can't be keys but tuples can 

        return list(res.values()) # just return the values 






        