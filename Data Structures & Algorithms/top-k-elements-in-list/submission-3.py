class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)

        for x in nums:
            hash[x] += 1;

        frequency: list[int] = [[] for i in range(len(nums)+1)]

        for key, val in hash.items():
            frequency[val].append(key)


        result: list[int] = []
        count = k;

        for i in range(len(nums), 0, -1):
            result.extend(frequency[i])

            count -= len(frequency[i])

            if count == 0:
                break

        

        return result; 
        