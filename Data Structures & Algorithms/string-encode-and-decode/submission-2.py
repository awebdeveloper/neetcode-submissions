class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""

        for item in strs:
            encodedStr += str(len(item)) + "#" + item 
        return encodedStr
            


    def decode(self, s: str) -> List[str]:
        index = 0;
        result: list[str] = []
        while index < len(s):
            innerIndex = index;
            while s[innerIndex] != '#':
                innerIndex += 1 

            keyLen = s[index : innerIndex];
            innerIndex += 1;
            end = innerIndex + int(keyLen);
            item = s[innerIndex: end]
            
            result.append(item)
            index = end

        return result