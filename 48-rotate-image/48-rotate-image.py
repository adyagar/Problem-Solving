class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        if len(matrix)>=2:
            
            matrix.reverse()
            for i in range(len(matrix)):
                for j in range(i+1,len(matrix[i])):
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
            
        