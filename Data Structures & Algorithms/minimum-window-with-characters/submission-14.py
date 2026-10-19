class Solution:
    def generateHash(self, s1: str) -> dict:
        s1Hash = {}
        for char in s1:
            s1Hash[char] = s1Hash.get(char,0) + 1
        return s1Hash

    def minWindow(self, s: str, t: str) -> str:
        tHash = self.generateHash(t)
        tLen = len(t)
        windowHash = {}
        res = ""

        if len(t) > len(s) or t == "":
            return ""

        left, right = 0, 0
        have, want = 0, len(tHash)
        for right in range(len(s)):
            if s[right] in tHash:
                windowHash[s[right]] = windowHash.get(s[right], 0) + 1

            if s[right] in tHash and windowHash[s[right]] == tHash[s[right]]:
                have += 1

            while have == want:
                if len(res) > right-left+1 or res == "":
                    res = s[left:right+1]

                if s[left] in tHash:
                    windowHash[s[left]] -= 1

                if s[left] in tHash and windowHash[s[left]] < tHash[s[left]]:
                    have -= 1

                left += 1
        return res