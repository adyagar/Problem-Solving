class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        a = 0 
        tot = 0
        b = len(mat) - 1
        for i in range(len(mat)):
            if a!=b:
                tot += mat[i][a] + mat[i][b]
            else:
                tot += mat[i][a]
            a+=1
            b-=1
        return tot
#             if i==j or i+j == len(mat) - 1:
#                     sum += mat[i][j]
#         return sum - mat[]
            