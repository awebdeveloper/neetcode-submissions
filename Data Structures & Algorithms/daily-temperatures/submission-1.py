class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temp)

        for i in range(len(temp)):
            while len(stack) > 0 and temp[i] > stack[-1][1]:
                ele = stack.pop()
                result[ele[0]] = i - ele[0] 

            stack.append((i,temp[i]))

        return result

'''
    0,30
        stack [(0,30)]

    1,38
        38>30
            stack []
            result[0] = 1-0 = 1
        stack [(1,38)]


    2, 30
        30>38: fail
        stack [(1,38)(2,30)]

    3, 36
        36>30
            stack [(1,38)]
            result[2] = 3-2 = 1
        stack [(1,38)(3,36)]

    4, 35
        35>36: fail
        stack [(1,38)(3,36)(4,35)]

    5, 40
        40>35:
            stack [(1,38)(3,36)]
            result[4] = 5-4 = 1
        
        40>36:
            stack [(1,38)]
            result[3] = 5-3 = 2

        40>38:
            stack []
            result[1] = 5-1 = 4
        stack [(5,40)]

    6, 20
        20>40: fail
        stack [(5,40)(6,20)]

'''