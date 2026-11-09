class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)
        if len(self.nums) > k:
            self.nums = self.nums[0:k]
        

    def add(self, val: int) -> int:
        sortInsert = False
        
        # number greater than kth number or total nums less than k, sort while inserting
        if len(self.nums) >= self.k and val > self.nums[-1] or len(self.nums) < self.k:
            sortInsert = True
            
        
        # sort while inserting
        if sortInsert == True:
            index = 0
            for i in range(len(self.nums)):
                if self.nums[i] < val:
                    index = i
                    break;

            self.nums.insert(index, val)
            if len(self.nums) > self.k:
                self.nums.pop()

        return self.nums[-1]


