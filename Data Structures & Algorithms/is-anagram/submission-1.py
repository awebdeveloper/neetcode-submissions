class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}

        if len(s) != len(t):
            return False
        
        for i in range(0,len(s)):
            hashS[s[i]] = hashS.get(s[i],0) + 1
            hashT[t[i]] = hashT.get(t[i],0) + 1

        for i in hashS:
            if hashS[i] != hashT.get(i,0):
                return False
        
        return True