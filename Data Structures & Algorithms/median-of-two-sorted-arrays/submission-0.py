class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = [0,0]

        max1 = len(nums1)
        max2 = len(nums2)
        counter1 = 0
        counter2 = 0

        mid = (max1+max2)//2

        while counter1 + counter2 <= mid:
            nextEle = None
            if counter1 == max1:
                nextEle = nums2[counter2]
                counter2 += 1
            elif counter2 == max2:
                nextEle = nums1[counter1]
                counter1 += 1
            else:
                nextEle = min(nums1[counter1], nums2[counter2])

                if nextEle == nums1[counter1]:
                    counter1 += 1
                else:
                    counter2 += 1

            res[0] = res[1]
            res[1] = nextEle
        print(res)

        return res[1] if (max1+max2)%2 != 0 else (res[1]+res[0])/2
