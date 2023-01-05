class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        
        n1 = len(original)
        
        if n*m !=n1:
            return []
        ans = [ [0]*n for i in range(m)] 
        temp = []
        for i in range(m):
            temp = original [n*i:n*i+n]
            print(temp)
            ans[i] = temp
        
        return ans
            