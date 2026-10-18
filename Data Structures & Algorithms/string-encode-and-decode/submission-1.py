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
            itemLen = ""
            innerIndex = index;
            key = s[innerIndex]
            while key != '#':
                itemLen += key
                innerIndex += 1 
                key = s[innerIndex];

            innerIndex += 1;
            end = innerIndex + int(itemLen);

            item = ""
            while innerIndex < end:
                item += s[innerIndex]
                innerIndex += 1
            
            result.append(item)
            index = end

        return result