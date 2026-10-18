class Solution:
    def check(self, s1Hash: dict, windowHash: dict) -> bool:
        for key in s1Hash:
            if not windowHash.get(key,0) == s1Hash[key]:
                return False
        return True

    def generateHash(self, s1: str) -> dict:
        s1Hash = {}
        for char in s1:
            s1Hash[char] = s1Hash.get(char,0) + 1
        return s1Hash

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False


        left = 0
        windowLength = len(s1);
        s1Hash = self.generateHash(s1)
        windowHash = self.generateHash(s2[left:windowLength])

        for left in range(len(s2)):
            right = left + windowLength - 1;
            if right >= len(s2):
                break;

            if left > 0:
                windowHash[s2[left-1]] -= 1
                windowHash[s2[right]] = windowHash.get(s2[right],0) + 1


            if self.check(s1Hash, windowHash):
                return True


        return False  