class Solution:
    
    def findMax (self, s:dict) -> tuple:
        biggestCount = 0
        biggestItem = None

        for key, value in s.items():
            if (value > biggestCount):
                biggestCount, biggestItem = value , key

        return (biggestItem, biggestCount)


    def characterReplacement(self, s: str, k: int) -> int:

        window = {}
        left = 0
        right = 0
        maxLen = 1

        while right < len(s):
            window[s[right]] = window.get(s[right],0) + 1
            windowLen = (right - left + 1)

            if  windowLen - self.findMax(window)[1] <= k:
                maxLen = max(maxLen, windowLen)
            else:
                window[s[left]] -= 1
                left += 1
            
            right += 1

        return maxLen