class Solution:

    def encode(self, strs: List[str]) -> str:
        # return a string 
        # a function that will organize the whole list in a string 
        # 4#neet

        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res



    def decode(self, s: str) -> List[str]:

        decodedList = []
        i = 0

        while i < len(s):
            j=i
            while s[j] != '#':
                j += 1
            length = s[i:j] # [0:1] -> 4
            i = 1 + j
            j = i + int(length) # 6
            decodedList.append(s[i:j]) # [2:6] -> [neet]
            
            i = j # new start 6 which is s[6] -> 4
            
        return decodedList 


