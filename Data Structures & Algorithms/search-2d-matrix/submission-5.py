class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])
        r,c = 0, cols-1

        while r<rows:
            
            if target <= matrix[r][c] and target >= matrix[r][0]:
                l = 0
                while l <= c: 
                    m = (l + c)//2
                    if matrix[r][m] > target:
                        c -= 1
                    elif matrix[r][m] < target:
                        l += 1
                    else:
                        return True
            
            else:
                r += 1 

                
                
        return False