class Solution:
    def isPalindrome(self, s: str) -> bool:
        # first out everything together -> take out the spaces
        # store it in a string unless if i can use the same string 
        # go through a loop looking through each char with-in the string 

        alnum_only = ""

        for char in s:
            if char.isalnum():
                alnum_only += char

        for i in range(len(alnum_only)):
            if alnum_only[i].lower() != alnum_only[-1 - i].lower():
                return False
        return True

        







        
        