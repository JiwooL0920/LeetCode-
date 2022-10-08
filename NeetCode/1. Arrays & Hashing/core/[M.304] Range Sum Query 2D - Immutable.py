# Given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:

# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity.

 

# Example 1:


# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]

# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

class NumMatrix:
    def __init__(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sumMat = [[0]*(COLS+1) for r in range(ROWS+1)]
        
        for r in range(ROWS):
            prefix = 0 
            for c in range(COLS):
                prefix += matrix[r][c] 
                # area of rectangle in above region
                above = self.sumMat[r][c+1]
                # placeholder 0s --> need to offset by 1
                self.sumMat[r+1][c+1] = prefix + above
                
        
    def sumRegion(self, r1, c1, r2, c2):
        # offset to access sum matrix
        r1, c1, r2, c2 = r1+1, c1+1, r2+1, c2+1 
        bottomRight = self.sumMat[r2][c2] 
        above = self.sumMat[r1-1][c2]
        left = self.sumMat[r2][c1-1] 
        