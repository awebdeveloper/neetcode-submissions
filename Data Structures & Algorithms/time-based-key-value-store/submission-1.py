class TimeMap:

    def __init__(self):
        self.hash = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if  key not in self.hash:
            self.hash[key] = [(value, timestamp)]
            
        else:
            self.hash[key].append((value, timestamp))
        


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash:
            return ""

        hash = self.hash[key]
        left, right = 0, len(hash) - 1

        while left <= right:
            mid = (left + right) // 2

            if  hash[mid][1] == timestamp:
                return hash[mid][0]
            elif hash[mid][1] < timestamp:
                left = mid+1
            else:
                right = mid-1

        return hash[right][0] if right >= 0 else ""


        
        

        




