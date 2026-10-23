class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [];
        maxArea = 0

        for i in range(len(heights)):
            index = i
            while len(stack) > 0 and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                
                #calculate area
                width = (i - index)
                area = height * width
                maxArea = max(maxArea, area)

            stack.append((index, heights[i]))

        for ele in stack:
            index, height = ele
            area = height * (len(heights) - index)
            maxArea = max(maxArea, area)
        
        return maxArea
