class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #find the row to search
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left+right) // 2

            if target > matrix[mid][-1]:
                left = mid+1
            elif target < matrix[mid][0]:
                right = mid-1
            else:
                break

        if not (left <= right):
            return False
            
        row = (left + right) // 2
        rowLeft, rowRight = 0, len(matrix[row]) - 1

        #find element in that row
        while rowLeft <= rowRight:
            mid = (rowLeft+rowRight) // 2
            
            if target > matrix[row][mid]:
                rowLeft = mid+1
            elif target < matrix[row][mid]:
                rowRight = mid-1
            elif target == matrix[row][mid]:
                return True
                    
        
        return False  


