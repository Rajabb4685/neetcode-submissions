class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap
        # if statement should check if the current str in sorted matches the key
        # if not then make a new key, and store the same value in it's original form 

        # give appropriate names for variables and names 
        # hashmap -> anagramGroups

        anagramGroups = {}

        for s in strs:
            sortedS = "".join(sorted(s))

            if sortedS in anagramGroups:
                anagramGroups[sortedS].append(s)
            else:
                anagramGroups[sortedS] = [s]

        return list(anagramGroups.values())
        