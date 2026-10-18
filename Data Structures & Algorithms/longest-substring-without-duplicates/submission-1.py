class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        found = []
        length = 0
        for char in s:
            if char in found:
                found  = found[found.index(char) + 1:]

            found.append(char)
            length = max(length, len(found))

        return length
        