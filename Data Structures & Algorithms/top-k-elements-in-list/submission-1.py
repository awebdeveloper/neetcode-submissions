class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = defaultdict(int)

        for x in nums:
            hash[x] += 1;

        result: list[int] = []

        for x, frequency in sorted(hash.items(), key=lambda x: x[1], reverse=True):
            result.append(x);

            if len(result) == k:
                break

        return result; 
        